using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Server
{
    class Program
    {
        private static readonly int _port = 8000;
        private static readonly string _address = "127.0.0.1";
        private static string _response;
        
        static async Task Main(string[] args)
        {
            Console.WriteLine($"Запуск сервера: {DateTime.Now.Date.ToString()}");
            
            try
            {
                TcpListener server = new TcpListener(IPAddress.Parse(_address), _port);
                server.Start();
 
                Console.WriteLine("Сервер запущен. Ожидание подключений...");
 
                while (true)
                {
                    TcpClient client = await server.AcceptTcpClientAsync();
                    Console.WriteLine($"Подключен клиент: {client.Client.RemoteEndPoint}");

                    Task.Run(() => HandleClient(client));
                }
            }
            catch(Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }

        private static async Task HandleClient(TcpClient client)
        {
            while (true)
            {
                NetworkStream stream = client.GetStream();

                byte[] buffer = new byte[1024];
                int bytes = await stream.ReadAsync(buffer, 0, buffer.Length);
                string request = Encoding.UTF8.GetString(buffer, 0, bytes);

                if (request == "exit")
                {
                    // Выход пользователя
                    byte[] response = Encoding.UTF8.GetBytes("EXIT");
                    await stream.WriteAsync(response, 0, response.Length);
                    Console.WriteLine($"Отключился клиент: {client.Client.RemoteEndPoint}");
                    client.Close();
                    break;
                }

                // Проверка на валидность сообщения
                Regex regex = new Regex(@"^[^\s:]+:[^\s:]+$");
                Match match = regex.Match(request);
                if (!match.Success)
                {
                    byte[] response = Encoding.UTF8.GetBytes("INCORRECT");
                    await stream.WriteAsync(response, 0, response.Length);
                    Console.WriteLine($"Невалидное сообщение от клиена: {client.Client.RemoteEndPoint}");
                }
                else
                {
                    string[] credentials = request.Split(':');
                    string username = credentials[0];
                    string password = credentials[1];

                    if (AuthenticateUser(username, password, client: client))
                    {
                        // Аутенфикация успешна
                        byte[] response = Encoding.UTF8.GetBytes("SUCCESS");
                        await stream.WriteAsync(response, 0, response.Length);
                        Console.WriteLine(_response);
                        client.Close();
                        break;
                    }
                    else
                    {
                        // Безуспешная аутенфикация
                        byte[] response = Encoding.UTF8.GetBytes("FAILURE");
                        await stream.WriteAsync(response, 0, response.Length);
                        Console.WriteLine(_response);
                    }
                }
            }
            
            return;
        }

        private static bool AuthenticateUser(string username, string pass, TcpClient client)
        {
            if (username != "user")
            {
                _response = $"Неверный логин у клиента: {client.Client.RemoteEndPoint}";
                return false;
            }

            if (pass != "user")
            {
                _response = $"Неверный пароль у клиента: {client.Client.RemoteEndPoint}";
                return false;
            }

            _response = $"Успешная авторизация у клиента: {client.Client.RemoteEndPoint}";
            return true;
        }
    }
}