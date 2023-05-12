using Microsoft.AspNetCore.SignalR;
using NetworkWebApp.Models;

namespace ChatWebApp.Hubs;

public class ChatHubs: Hub
{
    public async Task SendMessage(Message message) => await Clients.All.SendAsync("receiveMessage", message);
}