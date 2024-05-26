from Joueur import Joueur
from Terrain import Terrain
from LoyerHandler import (LoyerBanqueHandler, LoyerProprietaireHandler, 
                          LoyerHypothequeHandler, LoyerNuHandler, LoyerBatiHandler)

if __name__ == "__main__":
    banque = Joueur("Banque")
    vous = Joueur("Vous")
    rue_de_la_paix = Terrain("Rue de la Paix", proprietaire=banque)

 
 
    handler_banque = LoyerBanqueHandler()
    handler_proprietaire = LoyerProprietaireHandler(handler_banque)
    handler_hypotheque = LoyerHypothequeHandler(handler_proprietaire)
    handler_nu = LoyerNuHandler(handler_hypotheque)
    handler_bati = LoyerBatiHandler(handler_nu)

    #Terrain appartient à la banque
    print(f"Loyer (terrain à la banque): {handler_bati.calculer_loyer(rue_de_la_paix, vous)}")

    #Terrain vous appartient
    rue_de_la_paix.set_proprietaire(vous)
    print(f"Loyer (terrain vous appartient): {handler_bati.calculer_loyer(rue_de_la_paix, vous)}")

    #Terrain hypothéqué
    rue_de_la_paix.set_hypotheque(True)
    print(f"Loyer (terrain hypothéqué): {handler_bati.calculer_loyer(rue_de_la_paix, vous)}")

    #Terrain non hypothéqué et nu
    rue_de_la_paix.set_hypotheque(False)
    print(f"Loyer (terrain nu): {handler_bati.calculer_loyer(rue_de_la_paix, vous)}")

    #Construire une maison et calculer le loyer
    rue_de_la_paix.ajouter_maison()
    print(f"Loyer (1 maison): {handler_bati.calculer_loyer(rue_de_la_paix, vous)}")
    