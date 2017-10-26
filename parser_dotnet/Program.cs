using Newtonsoft.Json;

namespace parser_dotnet
{
    class Program
    {
        static void Main(string[] args)
        {
            var elem = new JsonSerializer().Deserialize(System.Console.In, typeof(System.Object));
            if (elem == null) throw new System.Exception();
        }
    }
}
