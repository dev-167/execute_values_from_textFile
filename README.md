# Text File Data Extractor

This Python script helps extract data from a large text file. It searches for specific patterns (e.g., city names) and outputs the corresponding values.

## Features

    Extracts specific columns from a text file
    Customizable search terms, e.g., for different cities
    Outputs the filtered data

## Usage

    Adjust the search term: Modify the search_term variable in the script to search for a different city or keyword.
    Provide the file: Ensure the text file is in the correct format and the file path is set correctly.
    Run the script: Execute the Python script to extract the data.

### Example:
´´´python
search_term = "Berlin"  # Change this to the desired search term (e.g., a city name)

## Anpassen des Regex-Patterns

Das **Regex-Pattern** in unserem Skript wird verwendet, um Daten aus einer Textdatei zu extrahieren.  
Aktuell sucht das Pattern nach Zeilen im Format:

| Stadt | Wert 1 | Wert 2 | Wert 3 |

### **Standard-Pattern im Code**
Im Code sieht das Pattern so aus:


pattern = re.compile(r"\|\s*(.*?)\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*([\d.]+)\s*\|")

(.*?) → Name der Stadt (dynamisch)
([\d,]+) → Erste Zahl (z. B. Umsatz)
([\d,]+) → Zweite Zahl (z. B. Verkäufe)
([\d.]+) → Dritte Zahl (z. B. Bestellwert)

### Eigene Anpassungen

Falls deine Datei eine zusätzliche Spalte enthält, z. B. "Rabatt", dann kannst du das Pattern erweitern:

pattern = re.compile(r"\|\s*(.*?)\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|")

## # Text File Data Extractor

This Python script helps extract data from a large text file. It searches for specific patterns (e.g., city names) and outputs the corresponding values.

## Features

    Extracts specific columns from a text file
    Customizable search terms, e.g., for different cities
    Outputs the filtered data

## Usage

    Adjust the search term: Modify the search_term variable in the script to search for a different city or keyword.
    Provide the file: Ensure the text file is in the correct format and the file path is set correctly.
    Run the script: Execute the Python script to extract the data.

### Example:
´´´python
search_term = "Berlin"  # Change this to the desired search term (e.g., a city name)

# Text File Data Extractor

This Python script helps extract data from a large text file. It searches for specific patterns (e.g., city names) and outputs the corresponding values.

## Features

    Extracts specific columns from a text file
    Customizable search terms, e.g., for different cities
    Outputs the filtered data

## Usage

    Adjust the search term: Modify the search_term variable in the script to search for a different city or keyword.
    Provide the file: Ensure the text file is in the correct format and the file path is set correctly.
    Run the script: Execute the Python script to extract the data.

### Example:
´´´python
search_term = "Berlin"  # Change this to the desired search term (e.g., a city name)

## Adjusting the Regex Pattern

The **Regex - pattern** in our script is used to extract data from a text file.
Currently, the pattern searches for lines in the format:

| City | Value 1 | Value 2 | Value 3 |

### **Standard-Pattern in the Code**
In the code, the pattern looks like this:


pattern = re.compile(r"\|\s*(.*?)\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*([\d.]+)\s*\|")

(.*?) → Name of the City (dynamic)
([\d,]+) → First number (e. g. revenue)
([\d,]+) → Second number (e. g. Sales)
([\d.]+) → Thrid number (e. g. Order Value)

### Custom Adjustments

If your file contains an additional column, e.g., "Discount," you can expand the pattern:

pattern = re.compile(r"\|\s*(.*?)\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|")

## If your File uses ; instead of |:

pattern = re.compile(r";\s*(.*?)\s*;\s*([\d,]+)\s*;\s*([\d,]+)\s*;\s*([\d.]+)\s*;")

## If you only want to extract data for Berlin

pattern = re.compile(r"\|\s*Berlin\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*([\d.]+)\s*\|")

```python