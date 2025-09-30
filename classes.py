# Definiera en klass Person med attributen namn och ålder
class Person:
    def __init__(self, namn, alder):
        self.namn = namn
        self.alder = alder

    def presentera(self):
        print(f"Jag heter {self.namn} och är {self.alder} år gammal.")

# Skapa ett objekt av klassen
p1 = Person("Said", 41)

# Anropa metoden för att skriva ut informationen
p1.presentera()


# Definiera en klass Bil
class Bil:
    def __init__(self, marke, arsmodell):
        self.marke = marke
        self.arsmodell = arsmodell

    def beskriv(self):
        print(f"Jag kör en {self.marke} från {self.arsmodell}.")

# Skapa ett objekt av klassen Bil
min_bil = Bil("Audi", 2020)

# Anropa metoden för att skriva ut informationen
min_bil.beskriv()


# Definiera en klass Hund

class Hund:
    def __init__(self, namn, ras):
        self.namn = namn
        self.ras = ras

    def skalla(self):
        print(f"{self.namn} säger this is a stick up!")
# Skapa ett objekt av klassen Hund
min_hund = Hund("Encro", "Pocketbully")
# anropa metoden för att få hunden att skälla
min_hund.skalla()