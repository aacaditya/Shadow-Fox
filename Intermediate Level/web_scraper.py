#  Web Scraper: Extracts data from websites using library BeautifulSoup and stores extracted data in a csv file. 
import requests
from bs4 import BeautifulSoup
import csv

url = "https://wikipedia.com"

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

print("Page Title : ",soup.title.text)

#lets extract h1 headings
h1_headings = soup.find_all("h1")
print("/nH1 headings : ")
for h1 in h1_headings:
    print(h1.text.strip())

#lets extract h2 headings
h2_headings = soup.find_all("h2")
print("/nH2 headings : ")
for h2 in h2_headings:
    print(h2.text.strip())

# Extract all links
all_links = soup.find_all("a")
print("/nAll Links :")
for link in all_links:
    href = link.get("href") #fetching hyperlinks
    
    if href and href.startswith("http"):
        print(href)

#extracting paragraphs 
para = soup.find_all("p")
print("/nParagraphs : ")
for p in para[:5] :
    print(p.text.strip())

# Now lets create a csv file that can store our extracted data : 

with open("Scraped_data.csv","w", newline="",encoding="utf-8") as file :
    writer = csv.writer(file)
    writer.writerow(["Heading type", "Text"])

    for h1 in h1_headings:
      writer.writerow(["H1",h1.text.strip()])

    for h2 in h2_headings:
      writer.writerow(["H2",h2.text.strip()])

print("Data saved in .csv file successfully!")
