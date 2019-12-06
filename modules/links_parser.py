from bs4 import BeautifulSoup as bs
from modules import session_generator


def run():

    # generation a new session
    request = session_generator.run('https://ru.wikipedia.org/wiki/Категория:Социологи_по_алфавиту')

    if request.status_code == 200:

        # getting all unordered lists
        soup = bs(request.content, 'html.parser')
        all_ul = soup\
            .find('div', attrs={'class', 'mw-category'})\
            .find_all('ul')

        # getting all list items
        all_li = []
        for li in all_ul:
            result = li.find_all('li')
            all_li.append(result)

        # getting all links wrappers
        all_a = []

        for a in all_li[0]:
            result = a.find_all('a')
            all_a.append(result)

        for a in all_li[1]:
            result = a.find_all('a')
            all_a.append(result)

        for a in all_li[2]:
            result = a.find_all('a')
            all_a.append(result)

        for a in all_li[3]:
            result = a.find_all('a')
            all_a.append(result)

        for a in all_li[4]:
            result = a.find_all('a')
            all_a.append(result)

        # getting all links values
        all_href = []
        for href in all_a:
            result = href[0]['href']
            all_href.append(result)

        return all_href

    else:
        return 'Connection error'


