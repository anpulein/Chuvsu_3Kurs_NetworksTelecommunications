using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace Client
{
    class Program
    {
        private static readonly int _port = 8000;
        private static readonly string _address = "127.0.0.1";
        private static TcpClient _client;
        private static NetworkStream _stream;
        
        static void Main(string[] args)
        {
            Console.WriteLine($"Запуск клиента: {DateTime.Now.Date.ToString()}");
            
            try
            {
                ConnectClient();              
                Console.WriteLine("Чтобы выйти напишите exit");

                while (true)
                {
                    Console.WriteLine("Введите имя пользователя и пароль (пример username:password):");
                    string input = Console.ReadLine();

                    _stream = _client.GetStream();
                    byte[] buffer = Encoding.UTF8.GetBytes(input);
                    _stream.Write(buffer, 0, buffer.Length);

                    buffer = new byte[1024];
                    int bytes = _stream.Read(buffer, 0, buffer.Length);
                    string response = Encoding.UTF8.GetString(buffer, 0, bytes);

                    if (!CheckResponse(response)) break;
                }

                DisconnectClient();
            }
            catch(Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            Console.WriteLine("Отключение системы...");
            return;
        }

        private static bool CheckResponse(string response)
        {
            switch (response)
            {
                case "SUCCESS":
                {
                    Console.WriteLine("Успешная аутенфикация!");
                    return false;
                }
                case "EXIT":
                {
                    return false;
                };
                case "INCORRECT":
                {
                    Console.WriteLine("Невалидное сообщение");
                    return true;
                }
                case "FAILURE":
                {
                    Console.WriteLine("Неправильный логин или пароль");
                    return true;
                }
                default: return true;
            }
        }

        private static void ConnectClient()
        {
            _client = new TcpClient();
            _client.Connect(_address, _port);
        }
        
        private static void DisconnectClient()
        {
            _stream.Close();
            _client.Close();
        }
    }
}