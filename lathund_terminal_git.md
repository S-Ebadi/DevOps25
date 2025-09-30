# Lathund: Terminal- och Git-kommandon för utveckling

## Navigering och filhantering

```bash
pwd                # Visa nuvarande katalog
ls                 # Lista filer och mappar
ls -l              # Detaljerad listning
ls -a              # Visa även dolda filer
cd <katalog>       # Byt katalog
cd ..              # Gå upp en nivå
cd ~               # Till hemkatalogen
mkdir <namn>       # Skapa ny mapp
rm <fil>           # Ta bort fil
rm -r <mapp>       # Ta bort mapp och innehåll
cp <källa> <mål>   # Kopiera fil/mapp
mv <källa> <mål>   # Flytta/byt namn på fil/mapp
cat <fil>          # Visa filinnehåll
less <fil>         # Bläddra i fil
open <fil>         # Öppna fil (macOS)
```

## Python & miljö

```bash
python --version                   # Visa Python-version
python <fil>.py                    # Kör Python-fil
python -m venv .venv               # Skapa virtuell miljö
source .venv/bin/activate          # Aktivera virtuell miljö (macOS/Linux)
.venv\Scripts\activate             # Aktivera (Windows)
pip install -r requirements.txt    # Installera beroenden
pip freeze > requirements.txt      # Spara aktuella beroenden
```

## Git – versionshantering

```bash
git init                           # Initiera nytt repo
git clone <url>                    # Klona repo
git status                         # Visa status
git add <fil>                      # Lägg till fil för commit
git add .                          # Lägg till alla ändringar
git commit -m "Meddelande"         # Spara ändringar
git log --oneline                  # Visa commit-historik
git diff                           # Visa ändringar
git branch                         # Lista grenar
git checkout <gren>                # Byt gren
git checkout -b <ny_gren>          # Skapa och byt till ny gren
git merge <gren>                   # Slå ihop gren
git pull                           # Hämta och slå ihop från remote
git push                           # Skicka ändringar till remote
git remote -v                      # Visa remote-url:er
git stash                          # Tillfälligt spara ändringar
git rm --cached <fil>              # Ta bort fil från versionshantering
```

## VS Code

```bash
code .                             # Starta VS Code i aktuell mapp
```

## Övrigt

```bash
history                            # Visa kommandohistorik
clear                              # Rensa terminalen
whoami                             # Visa användarnamn
date                               # Visa datum och tid
```

---

> Tips: Använd tab för autokomplettering och piltangenter för att bläddra i tidigare kommandon.
