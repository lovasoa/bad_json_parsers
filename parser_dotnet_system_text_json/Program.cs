using System;
using System.Text.Json;
using System.Threading.Tasks;

namespace ParserDotnetSystemTextJson
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var stdin = Console.OpenStandardInput();
            await JsonSerializer.DeserializeAsync(stdin, typeof(object));
        }
    }
}
