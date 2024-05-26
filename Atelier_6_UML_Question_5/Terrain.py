from Joueur import Joueur

class Terrain:
    def __init__(self, nom, proprietaire=None, hypotheque=False, maisons=0):
        self.nom = nom
        self.proprietaire = proprietaire
        self.hypotheque = hypotheque
        self.maisons = maisons

    def set_proprietaire(self, proprietaire):
        self.proprietaire = proprietaire

    def set_hypotheque(self, hypotheque):
        self.hypotheque = hypotheque

    def ajouter_maison(self):
        self.maisons += 1

