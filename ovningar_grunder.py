
# Övningar – Grundläggande Python

# 1. Skriv ut text
print("Hej, världen!")

# 2. Variabler och input
namn = input("Vad heter du? ")
print(f"Hej, {namn}!")

# 3. If-sats
tal = int(input("Mata in en siffra: "))
if tal > 10:
    print("Större än 10!")
else:
    print("10 eller mindre.")

# 4. Funktioner
def addera(a, b):
    return a + b

resultat = addera(3, 5)
print(resultat)

# 5. Klasser
class Person:
    def __init__(self, namn, alder):
        self.namn = namn
        self.alder = alder

    def presentera(self):
        print(f"Jag heter {self.namn} och är {self.alder} år.")

p = Person("Sara", 22)


# 6. Lista och loop
namnlista = ["Ali", "Sara", "Erik", "Maja", "Lina"]
for namn in namnlista:
    print(namn)

# 7. Importera och använda ett bibliotek
import psutil
print(psutil.cpu_percent(interval=1))
Skapa en klass Person med attributen namn och ålder. Skapa ett objekt och skriv ut informationen.
