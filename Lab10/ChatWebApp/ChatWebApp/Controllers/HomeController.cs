using System.Diagnostics;
using ChatWebApp.Data;
using Microsoft.AspNetCore.Mvc;
using ChatWebApp.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
using NetworkWebApp.Models;

namespace ChatWebApp.Controllers;
[Authorize]
public class HomeController : Controller
{
    private readonly ILogger<HomeController> _logger;
    private readonly ApplicationDbContext _context;
    private readonly UserManager<AppUser> _userManager;

    public HomeController(ILogger<HomeController> logger, ApplicationDbContext context, UserManager<AppUser> userManager)
    {
        _logger = logger;
        _context = context;
        _userManager = userManager;
    }
    
    public async Task<IActionResult> Index()
    {
        var currentUser = await _userManager.GetUserAsync(User);
        if (User.Identity.IsAuthenticated)
        {
            ViewBag.CurrentUserName = currentUser.UserName;
        }
        var messages = await _context.Message.Include(m => m.File).ToListAsync();
        return View("Index", messages);
    }
    
    [HttpPost]
    public async Task<IActionResult> Upload(IFormFile file)
    {
        var objFile = new Files();
        objFile.Id = Guid.NewGuid().ToString();
        objFile.ContentType = file.ContentType;

        var currentUser = await _userManager.GetUserAsync(User);
        if (User.Identity.IsAuthenticated)
        {
            ViewBag.CurrentUserName = currentUser.UserName;
        }

        var filename = System.IO.Path.GetFileName(file.FileName);
        var filePath = Path.Combine(Directory.GetCurrentDirectory(), "Upload", objFile.Id);
        
        objFile.Name = filename;
        objFile.Path = filePath;

        if (System.IO.File.Exists(filePath)) System.IO.File.Delete(filePath);

        await using (var localFile = System.IO.File.OpenWrite(filePath))
        {
            await using (var uploadedFile = file.OpenReadStream())
            {
                uploadedFile.CopyTo(localFile);
            }
        }
        
        
        await _context.Files.AddAsync(objFile);
        // await _context.SaveChangesAsync();

        Message message = new Message();
        message.UserName = User.Identity.Name;
        var sender = await _userManager.GetUserAsync(User);
        message.UserId = sender.Id;
        message.When = DateTime.Now;
        message.TypeMessage = TypeMessage.FILE;
        message.FileId = objFile.Id;
        message.Text = String.Empty;
        // message.File = objFile;
        await _context.Message.AddAsync(message);
        await _context.SaveChangesAsync();
        return Json(new {fileId = objFile.Id});
    }
    
    
    public async Task<IActionResult> Download(string fileName)
    {
        if (string.IsNullOrEmpty(fileName) || fileName == null)
        {
            return Content("File Name is Empty...");              
        }

        // get the filePath
        var file = await _context.Files.FirstOrDefaultAsync(f => f.Id == fileName);

        // create a memorystream
        var memoryStream = new MemoryStream();

        using (var stream = new FileStream(file.Path, FileMode.Open))
        {
            await stream.CopyToAsync(memoryStream);            
        }
        // set the position to return the file from
        memoryStream.Position = 0;
        
        return File(memoryStream, file.ContentType, file.Name);
    }

    public async Task<IActionResult> Create(Message message)
    {
        if (true)
        {
            message.UserName = User.Identity.Name;
            var sender = await _userManager.GetUserAsync(User);
            message.UserId = sender.Id;
            message.When = DateTime.Now;
            message.TypeMessage = TypeMessage.MESSAGE;
            await _context.Message.AddAsync(message);
            await _context.SaveChangesAsync();
            return Ok();
        }

        return Error();
    }

    public IActionResult Privacy()
    {
        return View();
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}