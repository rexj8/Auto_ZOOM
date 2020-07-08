import requests
from bs4 import BeautifulSoup

r = requests.get("http://glauniversity.in:8085/")
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)

title = soup.title
# print(title.string)

anch = soup.find_all('a')
# print(anch)

print(soup.find('p').get_text())
print(soup.get_text())