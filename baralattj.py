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

