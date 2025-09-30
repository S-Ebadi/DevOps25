
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

# 8. Skapa en klass Djur med attributen namn och art
class Djur:
    def __init__(self, namn, art):
        self.namn = namn
        self.art = art
    def beskriv(self):
        print(f"{self.namn} är en {self.art}.")
d1 = Djur("Leo", "Lejon")
d1.beskriv()

# 9. Skapa en lista med tal och skriv ut alla tal större än 5
tal_lista = [1, 3, 7, 10, 2, 6]
for t in tal_lista:
    if t > 5:
        print(t)

# 10. Funktion som returnerar om ett tal är jämnt eller udda
def ar_jamnt(tal):
    return "Jämnt" if tal % 2 == 0 else "Udda"
print(ar_jamnt(7))

# 11. Skapa en klass Bil med attribut och metod
class Bil:
    def __init__(self, marke, arsmodell):
        self.marke = marke
        self.arsmodell = arsmodell
    def beskriv(self):
        print(f"Jag kör en {self.marke} från {self.arsmodell}.")
bil1 = Bil("Toyota", 2018)
bil1.beskriv()

# 12. Skapa en lista med namn och sortera den
namn_lista = ["Anna", "Zara", "Erik", "Bo"]
namn_lista.sort()
print(namn_lista)

# 13. Funktion som räknar antalet vokaler i en sträng
def rakna_vokaler(text):
    return sum(1 for bokstav in text if bokstav.lower() in "aeiouyåäö")
print(rakna_vokaler("Hej världen"))

# 14. Skapa en klass Student med metod för att presentera sig
class Student:
    def __init__(self, namn, kurs):
        self.namn = namn
        self.kurs = kurs
    def presentera(self):
        print(f"Jag heter {self.namn} och läser {self.kurs}.")
s1 = Student("Maja", "Python")
s1.presentera()

# 15. Skapa en funktion som tar en lista och returnerar medelvärdet
def medelvarde(lista):
    return sum(lista) / len(lista)
print(medelvarde([2, 4, 6, 8]))

# 16. Skapa en klass Hund med metod för att skälla
class Hund:
    def __init__(self, namn):
        self.namn = namn
    def skalla(self):
        print(f"{self.namn} säger Voff!")
h = Hund("Bosse")
h.skalla()

# 17. Funktion som skriver ut multiplikationstabellen för ett tal
def multiplikationstabell(tal):
    for i in range(1, 11):
        print(f"{tal} x {i} = {tal*i}")
multiplikationstabell(5)

# 18. Skapa en klass Bok med attribut titel och författare
class Bok:
    def __init__(self, titel, forfattare):
        self.titel = titel
        self.forfattare = forfattare
    def info(self):
        print(f"{self.titel} av {self.forfattare}")
bok1 = Bok("Python 101", "S. Ebadi")
bok1.info()

# 19. Funktion som returnerar det största talet i en lista
def storsta_talet(lista):
    return max(lista)
print(storsta_talet([1, 9, 3, 7]))

# 20. Skapa en klass Konto med insättning och uttag
class Konto:
    def __init__(self, saldo):
        self.saldo = saldo
    def insattning(self, belopp):
        self.saldo += belopp
    def uttag(self, belopp):
        self.saldo -= belopp
    def visa_saldo(self):
        print(f"Saldo: {self.saldo}")
k = Konto(100)
k.insattning(50)
k.uttag(30)
k.visa_saldo()

# 21. Funktion som vänder en sträng
def vanda_strang(text):
    return text[::-1]
print(vanda_strang("Python"))

# 22. Skapa en klass Cykel med attribut och metod
class Cykel:
    def __init__(self, typ, hjul):
        self.typ = typ
        self.hjul = hjul
    def beskriv(self):
        print(f"En {self.typ} med {self.hjul} hjul.")
cykel1 = Cykel("Mountainbike", 2)
cykel1.beskriv()

# 23. Funktion som räknar antalet ord i en mening
def rakna_ord(mening):
    return len(mening.split())
print(rakna_ord("Detta är en mening."))

# 24. Skapa en klass Lärare med metod för att undervisa
class Larare:
    def __init__(self, namn, ämne):
        self.namn = namn
        self.amne = ämne
    def undervisa(self):
        print(f"{self.namn} undervisar i {self.amne}.")
larare1 = Larare("Ali", "Matematik")
larare1.undervisa()

# 25. Funktion som returnerar en lista med kvadrater av tal 1-10
def kvadrater():
    return [i**2 for i in range(1, 11)]
print(kvadrater())

# 26. Skapa en klass Film med attribut titel och genre
class Film:
    def __init__(self, titel, genre):
        self.titel = titel
        self.genre = genre
    def info(self):
        print(f"{self.titel} är en {self.genre}-film.")
film1 = Film("Inception", "Sci-Fi")
film1.info()

# 27. Funktion som kontrollerar om ett ord är ett palindrom
def ar_palindrom(ord):
    return ord == ord[::-1]
print(ar_palindrom("anna"))

# 28. Skapa en klass Mat med attribut namn och kalorier
class Mat:
    def __init__(self, namn, kalorier):
        self.namn = namn
        self.kalorier = kalorier
    def info(self):
        print(f"{self.namn} innehåller {self.kalorier} kalorier.")
mat1 = Mat("Banan", 89)
mat1.info()

# 29. Funktion som summerar alla tal i en lista
def summera(lista):
    return sum(lista)
print(summera([1, 2, 3, 4]))

# 30. Skapa en klass Mobil med attribut märke och modell
class Mobil:
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell
    def info(self):
        print(f"{self.marke} {self.modell}")
mobil1 = Mobil("Apple", "iPhone 13")
mobil1.info()

# 31. Funktion som returnerar alla jämna tal i en lista
def jamna_tal(lista):
    return [t for t in lista if t % 2 == 0]
print(jamna_tal([1, 2, 3, 4, 5, 6]))

# 32. Skapa en klass Konto med metod för att ändra ägare
class Konto2:
    def __init__(self, saldo, agare):
        self.saldo = saldo
        self.agare = agare
    def byt_agare(self, ny_agare):
        self.agare = ny_agare
    def info(self):
        print(f"Kontoägare: {self.agare}, Saldo: {self.saldo}")
k2 = Konto2(200, "Sara")
k2.byt_agare("Ali")
k2.info()

# 33. Funktion som räknar antalet tecken i en sträng
def rakna_tecken(text):
    return len(text)
print(rakna_tecken("Python"))

# 34. Skapa en klass Dator med attribut märke och RAM
class Dator:
    def __init__(self, marke, ram):
        self.marke = marke
        self.ram = ram
    def info(self):
        print(f"{self.marke} med {self.ram}GB RAM")
dator1 = Dator("Dell", 16)
dator1.info()

# 35. Funktion som returnerar summan av två tal
def summa(a, b):
    return a + b
print(summa(7, 8))

# 36. Skapa en klass Fågel med attribut namn och färg
class Fagel:
    def __init__(self, namn, farg):
        self.namn = namn
        self.farg = farg
    def info(self):
        print(f"{self.namn} är {self.farg}.")
fagel1 = Fagel("Papegoja", "grön")
fagel1.info()

# 37. Funktion som returnerar en lista med längder på ord
def ord_langder(lista):
    return [len(ord) for ord in lista]
print(ord_langder(["hej", "världen", "python"]))

# 38. Skapa en klass Programmerare med attribut namn och språk
class Programmerare:
    def __init__(self, namn, sprak):
        self.namn = namn
        self.sprak = sprak
    def info(self):
        print(f"{self.namn} programmerar i {self.sprak}.")
prog1 = Programmerare("Said", "Python")
prog1.info()

# 39. Funktion som returnerar det minsta talet i en lista
def minsta_talet(lista):
    return min(lista)
print(minsta_talet([5, 2, 9, 1]))

# 40. Skapa en klass Konto3 med metod för att räkna ränta
class Konto3:
    def __init__(self, saldo):
        self.saldo = saldo
    def rakna_ranta(self, procent):
        self.saldo += self.saldo * procent / 100
    def info(self):
        print(f"Saldo med ränta: {self.saldo}")
k3 = Konto3(1000)
k3.rakna_ranta(5)
k3.info()
