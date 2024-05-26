class LoyerHandler:
    def __init__(self, successeur=None):
        self.successeur = successeur

    def calculer_loyer(self, terrain, joueur):
        if self.successeur:
            return self.successeur.calculer_loyer(terrain, joueur)
        return 0


class LoyerBanqueHandler(LoyerHandler):
    def calculer_loyer(self, terrain, joueur):
        if terrain.proprietaire.nom == "Banque":
            return 0
        return super().calculer_loyer(terrain, joueur)


class LoyerProprietaireHandler(LoyerHandler):
    def calculer_loyer(self, terrain, joueur):
        if terrain.proprietaire == joueur:
            return 0
        return super().calculer_loyer(terrain, joueur)


class LoyerHypothequeHandler(LoyerHandler):
    def calculer_loyer(self, terrain, joueur):
        if terrain.hypotheque:
            return 0
        return super().calculer_loyer(terrain, joueur)


class LoyerNuHandler(LoyerHandler):
    def calculer_loyer(self, terrain, joueur):
        if terrain.maisons == 0:
            # Supposons que le loyer pour le terrain nu soit une valeur fixe, par exemple 200
            return 200
        return super().calculer_loyer(terrain, joueur)


class LoyerBatiHandler(LoyerHandler):
    def calculer_loyer(self, terrain, joueur):
        if terrain.maisons > 0:
            # Supposons une grille de loyer en fonction du nombre de maisons
            grille_loyer = {1: 500, 2: 1000, 3: 1500, 4: 2000, 5: 2500}
            return grille_loyer.get(terrain.maisons, 0)
        return super().calculer_loyer(terrain, joueur)

