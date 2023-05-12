using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Runtime.InteropServices.JavaScript;
using ChatWebApp.Models;
using Microsoft.EntityFrameworkCore;

namespace NetworkWebApp.Models;

public class Message
{
    public int Id { get; set; }
    [Required]
    public string UserName { get; set; }
    [Required]
    public string Text { get; set; }
    public DateTime When { get; set; }
    public String UserId { get; set; }
    public virtual AppUser Sender { get; set; }
    [EnumDataType(typeof(TypeMessage))]
    public TypeMessage TypeMessage { get; set; }
    public String? FileId { get; set; }
    public virtual Files? File { get; set; }
    public DateTime? b_deleted { get; set; }
}

public enum TypeMessage
{
    MESSAGE,
    FILE
}