using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;
using NetworkWebApp.Models;

namespace NetworkWebApp.Data;

public class ApplicationDbContext : IdentityDbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options) {}

    protected override void OnModelCreating(ModelBuilder builder)
    {
        base.OnModelCreating(builder);
        builder.Entity<Message>()
            .HasOne<AppUser>(a => a.AppUser)
            .WithMany(d => d.Messages)
            .HasForeignKey(d => d.UserId);
    }
}