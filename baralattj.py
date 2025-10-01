'''
# Skapa en namnlista och sortera den
namn_lista = ["Said", "Mika", "Levie", "Alexander", "Vincent"]
namn_lista.sort()
print(namn_lista)


def rakna_vokaler(text):
    return sum(1 for bokstav in text if bokstav.lower() in "aeiouyåäö")

text = input("Vill du räkna vokaler? Skriv in en text: ")
antal_vokaler = rakna_vokaler(text)

# Ett exempel
print(f"Det fanns {antal_vokaler} vokaler i din text!")
# Ett annat...
print(f"Det fanns {antal_vokaler} vokaler i \"{text}\"")


def multiplikationstabell(tal):
    for i in range(1,11):
        print(f"{tal} * {i} = {tal*i}")
multiplikationstabell(8)

'''

class Konto:
    def __init__(self, saldo):
        self.saldo = saldo
    def insattning(self, belopp):
        self.saldo += belopp
    def uttag(self, belopp):
        self.saldo -= belopp
    def visa_saldo(self):
        print(f"Saldo: {self.saldo}")
k = Konto(967)
k.insattning(500)
k.uttag(500)
k.visa_saldo()

