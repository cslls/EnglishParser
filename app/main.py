from bs4 import BeautifulSoup
import requests

url = input("📄 Введите ссылку на статью: ")
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

content = []
filteredContent = []

content = soup.findAll('div', class_='content')

for data in content:
    if data.find('p') is not None:
        filteredContent.append(data.text)

for data in filteredContent:
    print(data)
