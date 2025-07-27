

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

#fetching page content
url = "https://test-scrape-site.onrender.com/tech-gadgets.html"
response = requests.get(url)


#getting the html content
soup = BeautifulSoup(response.content, "html.parser")
cards = soup.find_all("div", class_="gadget")


#Excel file
wb = Workbook()
ws = wb.active
ws.title = "Tech Gadgets"
ws.append(["Product Name", "Description","brand","Year","Price"])

#reading and writing the data

for card in cards:
    name = card.find("h3").get_text(strip=True)
    description = card.find("p", class_ ="description").get_text(strip=True)
    brand = card.find("p", class_="brand").get_text(strip=True)
    year = card.find("p",class_="year").get_text(strip=True)
    price = card.find("p",class_="price").get_text(strip=True)
    ws.append([name, description, brand, year ,price])


#saving the excell file

excel_fileName = "tech-gadgets.xlsx"
wb.save(excel_fileName)

print("Scraping completed successfully")


