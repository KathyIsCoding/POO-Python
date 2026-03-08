# AJOUT : Une méthode pour faire une action
class VoitureDeLuxe:
    def __init__(self, marque):
        self.marque = marque
        self.vitesse = 0

    def accelerer(self, valeur):
        self.vitesse += valeur
        print(f"La {self.marque} roule maintenant à {self.vitesse} km/h")

v1 = VoitureDeLuxe("Lamborghini")
v1.accelerer(50)