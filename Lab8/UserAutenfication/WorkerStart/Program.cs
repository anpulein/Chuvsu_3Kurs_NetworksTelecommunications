using System;
using System.Diagnostics;

namespace WorkerStart
{
    
    class Program
    {
        private static ProcessStartInfo startService = new ProcessStartInfo()
        {
            FileName = "bin\\Debug\\net5.0\\Server.exe",
            CreateNoWindow = false,
            UseShellExecute = false,
            RedirectStandardOutput = true,
            RedirectStandardError = true
        };
        
        private static ProcessStartInfo startClient1 = new ProcessStartInfo()
        {
            FileName = "D:\\Projects\\Chuvsu_3Kurs_NetworksTelecommunications\\Lab8\\UserAutenfication\\Client\\bin\\Debug\\net5.0\\Client.exe",
            CreateNoWindow = true,
            UseShellExecute = false,
            RedirectStandardOutput = true,
            RedirectStandardError = true
        };
        
        private static ProcessStartInfo startClient2 = new ProcessStartInfo()
        {
            FileName = "D:\\Projects\\Chuvsu_3Kurs_NetworksTelecommunications\\Lab8\\UserAutenfication\\Client\\bin\\Debug\\net5.0\\Client.exe",
            CreateNoWindow = true,
            UseShellExecute = false,
            RedirectStandardOutput = true,
            RedirectStandardError = true
        };

        private static Process _process;
        
        static void Main(string[] args)
        {
            _process = new Process();

            _process.StartInfo = startService;
            _process.Start();

            _process.WaitForExitAsync();

            // _process.StartInfo = startClient1;
            // _process.Start();
            //
            // _process.StartInfo = startClient2;
            // _process.Start();
        }
    }
}