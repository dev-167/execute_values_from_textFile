# Import modules | re = Regex for pattern definition | os = Operating system functions
import re
import os

# Define your search term
search_term = "Berlin"

# File path containing the text files
file_path = "text_files/text_file_1.txt"

# Check if the file exists
if not os.path.exists(file_path):
    print(f"Error: The file '{file_path}' does not exist!")
    exit()  # Exit the program if the file is missing

# 1. Here, a regex pattern is created that will later be used  
# to filter out data related to the Berlin branch from a line in the text file.
# Regex pattern
pattern = re.compile(r"\|\s*(.*?)\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*([\d.]+)\s*\|")

# Open the file and read its content
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# Search for a specific pattern
match = pattern.search(content)

# Output the result
# If a match is found, we can extract the data
if match:
    # Create a dictionary for the groups
    group_names = ['Search Term', 'Revenue', 'Sales', 'Order Value']
    group_data = match.groups()

    # Create a dynamic dictionary where the names are assigned to the groups
    data_dict = {group_names[i]: group_data[i] for i in range(len(group_names))}

    # Output the extracted data with dynamic labels
    print(f"{data_dict['Search Term']} : Revenue = {data_dict['Revenue']}, Sales = {data_dict['Sales']}, Order Value = {data_dict['Order Value']}")
else:
    print("No match found.")
