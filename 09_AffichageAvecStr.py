#La méthode spéciale `__str__` (L'affichage plus propre)
class VoitureDeLuxe:
    def __init__(self, marque):
        self.marque = marque

    def __str__(self):
        return f"[Voiture de Luxe : {self.marque}]"

v1 = VoitureDeLuxe("Ferrari")
print(v1) # Affiche : [Voiture de Luxe : Ferrari]
