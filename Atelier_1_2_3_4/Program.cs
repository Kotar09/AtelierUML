using CollabProjet.Products;

namespace CollabProjet
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Exo1();
            Exo2();
        }

        static void Exo1()
        {
            var b1 = Banque.GetInstance();
            b1.Cash = 1000;
            Console.WriteLine(b1.Cash);

            var b2 = Banque.GetInstance();
            b2.Cash = 500;
            Console.WriteLine(b2.Cash);
            Console.WriteLine(b1.Cash + "\n");
        }

        static void Exo2()
        {
            var factory = new BuyableFactory();

            var rue1 = factory.Make<Terrain>("Rue de la Paix", 400);
            var rue2 = factory.Make<Terrain>("Rue de Courcelles", 100);
            Console.WriteLine($"{rue1.Name} - {rue1.Price} euro(s)");
            Console.WriteLine($"{rue2.Name} - {rue2.Price} euro(s)");

            var gare1 = factory.Make<Gare>("Montparnasse", 200);
            Console.WriteLine($"{gare1.Name} - {gare1.Price} euro(s)" + "\n");
        }
    }
}
