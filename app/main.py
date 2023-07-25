from bs4 import BeautifulSoup
import requests
import datetime

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

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")

file_name = f"{current_time}.txt"
file_path = "results/" + file_name

with open(file_path, "w+") as txt_file:
    txt_file.write(data)
txt_file.close()