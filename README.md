# Text File Data Extractor – Extract Structured Data from Large Text Files

This Python script helps extract data from a large text file. It searches for specific patterns (e.g., city names) and outputs the corresponding values.

## Introduction

This Python script helps extract structured data from large text files using regular expressions (Regex). It is useful for data analysts, developers, or anyone working with large datasets in text format.
The script searches for specific patterns (e.g., city names) and extracts corresponding numerical values such as revenue, sales, and order values.


## Features

    Extracts specific columns from a text file
    Customizable search terms, e.g., for different cities
    Outputs the filtered data

## Usage

    Adjust the search term: Modify the search_term variable in the script to search for a different city or keyword.
    Provide the file: Ensure the text file is in the correct format and the file path is set correctly.
    Run the script: Execute the Python script to extract the data.

### Modify the search term:

Open the script and change the search_term variable:

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

### Run the script

python execute_values_from_textFile.py

### Custom Adjustments

If your file contains an additional column, e.g., "Discount," you can expand the pattern:

pattern = re.compile(r"\|\s*(.*?)\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|")

If your File uses ; instead of |:

pattern = re.compile(r";\s*(.*?)\s*;\s*([\d,]+)\s*;\s*([\d,]+)\s*;\s*([\d.]+)\s*;")

If you only want to extract data for Berlin

pattern = re.compile(r"\|\s*Berlin\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*([\d.]+)\s*\|")

```python
