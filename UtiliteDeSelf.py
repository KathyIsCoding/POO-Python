class VoitureDeLuxe:
    def __init__(self, marque):
        self.marque = marque

    def afficher_marque(self):
        print(f"La voiture est une {self.marque}.")

voiture_01 = VoitureDeLuxe("Lamborghini")
#methode1(on utilise la méthode directement sur l'objet/l'instance)
voiture_01.afficher_marque()
#methode2 (en passant par la classe on spécifie l'objet)
VoitureDeLuxe.afficher_marque(voiture_01)