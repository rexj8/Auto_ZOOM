import requests
from bs4 import BeautifulSoup

r = requests.get("http://glauniversity.in:8085/")
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)

