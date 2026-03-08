#On crée un compteur d'objets à partir d'un attribut statique
#On n'oublie pas le self dans la méthode
class VoitureDeLuxe:

    voitures_crees = 0

    def __init__(self, marque):
        VoitureDeLuxe.voitures_crees += 1
        self.marque = marque

voiture_01 = VoitureDeLuxe("Lamborghini")
voiture_02 = VoitureDeLuxe("Porsche")

print(voiture_01.marque)
print(voiture_02.marque)

print("Nombre de voitures créées :", VoitureDeLuxe.voitures_crees)