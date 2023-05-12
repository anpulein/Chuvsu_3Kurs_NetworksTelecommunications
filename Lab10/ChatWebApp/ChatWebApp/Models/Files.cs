using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using NetworkWebApp.Models;

namespace ChatWebApp.Models;

public class Files
{
    [Key]
    public virtual string Id { get; set; }
    public string Name { get; set; }
    public string Path { get; set; }
    public string ContentType { get; set; }
    public DateTime? b_deleted { get; set; }

    // Ссылка на Message
    public virtual Message Message { get; set; }
}
