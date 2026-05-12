# Link Extractor
# A.I Disclaimer: Some, I used A.I to fix syntax errors
import re
import os

input_file = input("Enter input filename: ")

if not os.path.exists(input_file):
    print("Error: File does not exist.")
    exit()

output_file = input("Enter output filename: ")

with open(input_file, "r") as file:
    content = file.read()

pattern = r"https?://\S+"

links = re.findall(pattern, content)

with open(output_file, "w") as file:
    for link in links:
        file.write(link + "\n")

# Print results
print(f"Found {len(links)} links.")
print(f"Links written to {output_file}.")