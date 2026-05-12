Link Extractor

Write a Python program that reads a text file, finds links using regular expressions, and writes just the links to a new file.

Requirements:

Prompt the user for an input filename.
If the file does not exist, display an error and exit.
Use regex/regular expressions to find links.
Find links that start with http:// or https://.
Write only the links to an output file.
Prompt the user for the output filename.
Print how many links were found.
Example Input File:

Here is a website: https://ualr.edu
Here is another one: http://example.com/page
This line has no link.
Example Output File:

https://ualr.edu
http://example.com/page
Example Program Run:

Enter input filename: links.txt
Enter output filename: found_links.txt
Found 2 links.
Links written to found_links.txt.
