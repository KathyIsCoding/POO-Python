#On initialise les obejts à partir de la méthode spéciale __init__
class VoitureDeLuxe:

    def __init__(self, marque):
        self.marque = marque

voiture_01 = VoitureDeLuxe("Lamborghini")
voiture_02 = VoitureDeLuxe("Porsche")

print(voiture_01.marque)
print(voiture_02.marque)