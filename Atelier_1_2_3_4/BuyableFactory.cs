using CollabProjet.Products;

namespace CollabProjet
{
    public class BuyableFactory
    {
        public BuyableProduct Make<T>(string name, int price) where T : BuyableProduct
        {
            var value = typeof(T);

            return value switch
            {
                Type t when t == typeof(Gare) => new Gare() { Name = name, Price = price },
                Type t when t == typeof(Compagnie) => new Compagnie() { Name = name, Price = price },
                Type t when t == typeof(Terrain) => new Terrain() { Name = name, Price = price },
                _ => throw new NotImplementedException()
            };
        }
    }
}
