# Import libraries
import requests
import os
import datetime
from bs4 import BeautifulSoup

# URL from which pdfs to be downloaded
url = "https://www.gob.mx/jfca/documentos/boletin-laboral-mayo-2023?idiom=es"

# Requests URL and get response object
response = requests.get(url)

# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')

# Find all hyperlinks present on webpage
links = soup.find_all('a')
#print ( links)
i = 0

# From all links check for pdf link and
# if present download file
for link in links:
    href_str = link['href']
    current_date = datetime.datetime.now().strftime("%m-%d-%Y")
    link_pdf = "https://www.gob.mx/" + href_str
    if '.pdf' in link_pdf:
        i += 1
        print("Downloading file: ", i)

        # Get response object for link
        response = requests.get(link_pdf)

        # Write content in pdf file
        pdf = open("pdf"+str(i)+".pdf", 'wb')
        pdf.write(response.content)
        pdf.close()
        print("File ", i, " downloaded")
        new_filename = f'Boletin Laboral CDMX {current_date}.pdf'
        os.rename("pdf1.pdf", new_filename)
        break
print("All PDF files downloaded")
