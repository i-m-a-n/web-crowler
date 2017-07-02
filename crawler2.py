import dryscrape
from bs4 import BeautifulSoup

result = open ("result2.txt",'w')
session = dryscrape.Session()
session.visit("http://digikala.com")
response = session.body()

soup = BeautifulSoup(response,"lxml")
for product in soup.find_all('a',class_="productItem"):
    if product.find(class_="old-price") != None :
        href = "http://digikala.com"+product.get("href")
        oldPrice = product.find(class_="old-price").get_text()
        finalPrice = product.find(class_="final-price").get_text().split('<')[0]
        result.write('{:<11}  {:<11}  {:<100}'.format(oldPrice,finalPrice,href)+'\n')
