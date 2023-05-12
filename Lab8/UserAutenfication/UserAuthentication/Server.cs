using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace UserAuthentication
{
    public class Server
    {
        public static void Start()
        {
            // получаем адреса для запуска сокета
            IPEndPoint ipPoint = new IPEndPoint(IPAddress.Parse(Program.Address), Program.Port);
             
            // создаем сокет
            Socket listenSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
/*
Accept(): создает новый объект Socket для обработки входящего подключения
Bind(): связывает объект Socket с локальной конечной точкой
Close(): закрывает сокет
Connect(): устанавливает соединение с удаленным хостом
Listen(): начинает прослушивание входящих запросов
Poll(): определяет состояние сокета
Receive(): получает данные
Send(): отправляет данные
Shutdown(): блокирует на сокете прием и отправку данных
*/
            try
            {
                // связываем сокет с локальной точкой, по которой будем принимать данные
                listenSocket.Bind(ipPoint);
 
                // начинаем прослушивание
                listenSocket.Listen(10);
 
                Console.WriteLine("Сервер запущен. Ожидание подключений...");
 
                while (true)
                {
                    Socket handler = listenSocket.Accept();
                    // получаем сообщение
                    StringBuilder builder = new StringBuilder();
                    int bytes = 0; // количество полученных байтов
                    byte[] data = new byte[256]; // буфер для получаемых данных
 
                    do
                    {
                        bytes = handler.Receive(data);
                        builder.Append(Encoding.Unicode.GetString(data, 0, bytes));
                    }
                    while (handler.Available>0);
 
                    Console.WriteLine(DateTime.Now.ToShortTimeString() + ": " + builder.ToString());
 
                    // отправляем ответ
                    string message = "ваше сообщение доставлено";
                    data = Encoding.Unicode.GetBytes(message);
                    handler.Send(data);
                    // закрываем сокет
                    handler.Shutdown(SocketShutdown.Both);
                    handler.Close();
                }
            }
            catch(Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }
}