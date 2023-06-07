using ChatWebApp.Models;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;
using NetworkWebApp.Models;

namespace ChatWebApp.Data;

public class ApplicationDbContext : IdentityDbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {
    }
    
    protected override void OnModelCreating(ModelBuilder builder)
    {
        base.OnModelCreating(builder);
        builder.Entity<Message>()
            .HasOne<AppUser>(a => a.Sender)
            .WithMany(d => d.Messages)
            .HasForeignKey(d => d.UserId);

        builder.Entity<Message>()
            .HasOne<Files>(m => m.File)
            .WithOne(f => f.Message)
            .HasForeignKey<Message>(f => f.FileId); // добавляем внешний ключ на Id в таблице Files
    }
    
    public DbSet<Message> Message { get; set; }
    public DbSet<Files> Files { get; set; }
}