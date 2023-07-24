from bs4 import BeautifulSoup
import requests

url = 'https://learnenglish.britishcouncil.org/'
page = requests.get(url)
print(page.status_code)
soup = BeautifulSoup(page.text, "html.parser")
print(soup)
