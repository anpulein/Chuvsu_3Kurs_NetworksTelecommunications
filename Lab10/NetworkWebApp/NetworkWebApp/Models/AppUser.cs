using System.Collections.ObjectModel;
using Microsoft.AspNetCore.Identity;

namespace NetworkWebApp.Models;

public class AppUser : IdentityUser
{

    public AppUser()
    {
        Messages = new HashSet<Message>();
    }
    
    public virtual ICollection<Message> Messages { get; set; }
}