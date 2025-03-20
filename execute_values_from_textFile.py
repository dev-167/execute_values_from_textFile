ordner_pfad = "text_files/"
#Module importieren | re = Regex für Muster definition | os = Betriebssystemfunktionen
import re
import os



# Ordnerpfad, der die Textdateien enthält
ordner_pfad = "text_files/"

if not os.path.exists(ordner_pfad):
    os.makedirs(ordner_pfad)

# Regex für Verkaufsanalyse ( Berlin )
#Hier wird ein Regex-Muster zusammengestellt, das später verwendet wird, 
#um aus einer Zeile der Textdatei die Daten der Filiale Berlin herauszufiltern.
filiale_muster_berlin = re.compile(r"\|\s*Berlin\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*([\d.]+)\s*\|")

# Funktion zur Verarbeitung einer einzelnen Datei
#nimmt einen Dateipfad entgegen und gibt ein Dictionary mit den extrahierten Daten zurück.
def verarbeite_datei(datei_pfad):
    value_reihe_berlin = []
#Initialisiert leere Liste, der extrahierten Daten der Filiale Berlin gesammelt werden.

#Datei wird geöffnet, öfnet die Datei im Lese-Modus unter Verwendung der UTF-8-Kodierung
    with open(datei_pfad, "r", encoding="utf-8") as datei:
        #Zeilenweise Durchlaufen der Datei:
        for zeile in datei:
            #Regex - Muster Suche in jeder Zeile
            #Wenn ein Treffer (Match) gefunden wird, wird er in der Variable "treffer" gespeichert.
            if (treffer := filiale_muster_berlin.search(zeile)):
                value_reihe_berlin.append("\t".join(treffer.groups()))  # Alle Werte zusammenfügen
            #"\t".join(...) verbindet diese Werte zu einem String, getrennt durch Tabulatoren, sodass sie als TSV-Spalte dargestellt werden.


    # Rückgabe der extrahierten Daten als Dictionary
    # Die FUnktion gibt ein Dictionary zurück, bei dem der Schlüssel "Berlin" auf die Liste value_reihe_berlin verweist.
    return {
        "Berlin": value_reihe_berlin,
    }


# Verarbeitung aller Dateien im Ordner
ergebnisse = []
for datei_name in sorted(os.listdir(ordner_pfad)): #os.listdir(ordner_pfad) Listet alle angegebenen Ordner text_files/ auf. sortet(..) sortiert die Dateinamen, sodass sie in einer definierten Reihenfolge abgearbeitet werden.
    if datei_name.endswith(".txt"):  # Nur Textdateien verarbeiten # stellt sicher, dass nur Dateien mit der Endung .txt verarbeitet werden.
        datei_pfad = os.path.join(ordner_pfad, datei_name) # os.path.join(ordner_pfad,datei_name) kombiniert den Ordnerpfad mit dem Dateinamen, um den vollständigwen Pfad zur Datei zu erstellen
        daten = verarbeite_datei(datei_pfad) #Die Funktion wird für jede gefundene Textdatei aufgerufen, und die extrahierten Daten werden in der Variable daten gespeichert.
        ergebnisse.append((datei_name, daten)) # ergebnisse ist eine Liste, in der jedes Element ein Tupel aus dem Dateinamen und dem zugehörigen Daten-Dictionary ( hier mit dem Schlüssel "Berlin") ist.


# Neue TSV Datei wird erstellt (bzw. überschrieben)
with open("output_alle_dateien_verkaufsanalyse.tsv", "w", encoding="utf-8") as tsv_datei:
    # Kopfzeile schreiben
    tsv_datei.write("Umsatz\tVerkäufe\tBestellwert\n")
    
    for datei_name, daten in ergebnisse: #Iteriert über alle Tupel, die den Dateinamen und das zugehörige Daten-Dictionary enthalten.
        #Dateiname hinzufügen
        #tsv_datei.write(f"{datei_name}\t")
        if daten["Berlin"]: #Überprüft ob Daten für Berlin vorhanden sind
            
            for zeile in daten["Berlin"]:             #Iteriert über jede extrahierte Zeile (die zuvor mit Tabulatoren getrennt wurde) aus der Datei.
                tsv_datei.write(f"{datei_name}\t{zeile}\n") #Schreibt eine Zeile in die TSV-Datei, die den Dateinamen, einen Tabulator, den Inhalt der Zeile und einen Zeilenumbruch enthält.

print("Die Daten wurden erfolgreich in 'output_alle_dateien_verkaufsanalyse.tsv' geschrieben.")


#Dokumentation

#Zusammenfassung

#   Module importieren:
#   Ermöglicht den Zugriff auf Regex- und OS-Funktionen.

#   Dateien laden:
#   Durchsucht den Ordner text_files/ nach .txt-Dateien.

#   Regex anwenden:
#   Das Muster sucht in jeder Zeile der Dateien nach der Zeile, die zur Filiale Berlin gehört, und extrahiert Umsatz, Verkäufe und Bestellwert.

#   Daten extrahieren:
#   Die Funktion verarbeite_datei sammelt die extrahierten Werte in einer Liste.

#   Ergebnisse sammeln:
#   Alle Ergebnisse werden in der Liste ergebnisse gespeichert, wobei jedes Element ein Tupel aus Dateiname und extrahierten Daten ist.

#   TSV-Datei schreiben:
#   Die Ergebnisse werden in eine neue TSV-Datei exportiert, wobei jede Zeile den Dateinamen und die zugehörigen Verkaufsdaten enthält.

#   Abschlussmeldung:
#   Eine Nachricht bestätigt, dass der Export erfolgreich war.