import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

def search_articles(query, num_pages=1):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    links = []
    for page in range(num_pages):
        # Формируем URL для запроса
        url = f'https://www.google.com/search?q={query}&start={page}'

        # Отправляем HTTP-запрос к Google с указанными заголовками
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка статуса ответа

        # Используем BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ищем результаты поиска
        search_results = soup.find_all('div', class_='tF2Cxc')

        # Извлекаем заголовок и ссылку для каждого результата
        for result in search_results:
            title = result.find('h3').get_text()
            link = result.find('a')['href']
            links.append((title, link))

    return links

if __name__ == "__main__":
    query = input("Ваш запрос: ")
    num_pages = 2

    links = search_articles(query, num_pages)

    for number, (title, link) in enumerate(links, 1):
        print(f"{number} - {title} - {link}")

    # Сохраняем ссылки в Excel-файл
    df = pd.DataFrame(links, columns=['Title', 'Link'])
    df.index += 1
    path = "results/" + query + ".xlsx"
    df.to_excel(path, index_label='Number')
