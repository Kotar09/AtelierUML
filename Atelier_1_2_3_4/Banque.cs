namespace CollabProjet
{
    public class Banque
    {
        private static Banque _instance;
        public int Cash { get; set; }

        private Banque() { }

        public static Banque GetInstance()
        {
            _instance ??= new Banque();
            return _instance;
        }
    }
}
