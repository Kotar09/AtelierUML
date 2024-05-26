namespace CollabProjet
{
    public class Plateau
    {
        public Case[] cases { get; set; }

        public void AddCase(Case c)
        {

        }

        public Case GetCase()
        {
            return new();
        }

        public int CountCase()
        {
            return cases.Length;
        }
    }
}
