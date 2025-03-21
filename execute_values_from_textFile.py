#Module importieren | re = Regex für Muster definition | os = Betriebssystemfunktionen
import re
import os

# Nenne dein Suchbegriff
suchbegriff = "Berlin"

# Dateipfad, der die Textdateien enthält
datei_pfad = "text_files/text_file_1.txt"


# Prüfe ob die Datei existiert
if not os.path.exists(datei_pfad):
    print(f"Fehler: Die Datei '{datei_pfad} existiert nicht!")
    exit() # Programm beenden wenn die Datei fehlt

# 1. Hier wird ein Regex-Muster zusammengestellt, das später verwendet wird, 
#um aus einer Zeile der Textdatei die Daten der Filiale Berlin herauszufiltern.
#Regex-Muster
muster = re.compile(r"\|\s*(.*?)\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*([\d.]+)\s*\|")

# Datei öffnen und Inhalt lesen
with open(datei_pfad, "r", encoding="utf-8") as datei:
    inhalt = datei.read()

# Suche nach einem bestimmten Muster
match = muster.search(inhalt)

# Ergebnis ausgeben
# Wenn ein Treffer gefunden wird, können wir die Daten extrahieren
if match:
    # Erstellen eines Dictionaries für die Gruppen
    gruppen_namen = ['Suchbegriff', 'Umsatz', 'Verkäufe', 'Bestellwert']
    gruppen_daten = match.groups()

    # Dynamisches Dictionary erstellen, bei dem die Namen den Gruppen zugeordnet werden
    daten_dict = {gruppen_namen[i]: gruppen_daten[i] for i in range(len(gruppen_namen))}

    # Ausgabe der extrahierten Daten mit den dynamischen Bezeichnern
    print(f"{daten_dict['Suchbegriff']} : Umsatz = {daten_dict['Umsatz']}, Verkäufe = {daten_dict['Verkäufe']}, Bestellwert = {daten_dict['Bestellwert']}")
else:
    print("Kein Treffer gefunden.")