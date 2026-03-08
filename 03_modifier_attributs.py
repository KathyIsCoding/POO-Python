#Différence attribut de classe vs attribut d’instance
class VoitureDeLuxe:

    marque = "Lamborghini"

voiture_01 = VoitureDeLuxe()
voiture_02 = VoitureDeLuxe()

#Modifier au niveau de la classe
VoitureDeLuxe.marque = "Porsche"

#Modifier au niveau des objets
voiture_01.marque = "Peugeot"
voiture_02.marque = "Volkswagen"

print(VoitureDeLuxe.marque)
print(voiture_01.marque)
print(voiture_02.marque)