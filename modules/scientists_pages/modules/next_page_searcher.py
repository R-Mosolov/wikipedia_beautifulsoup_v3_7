from bs4 import BeautifulSoup as bs
from modules import session_generator


def run():
    # generation a new session
    request = session_generator.run('https://ru.wikipedia.org/wiki/Категория:Социологи_по_алфавиту')

    if request.status_code == 200:

        # getting the part link
        soup = bs(request.content, 'lxml')
        part_page_link = soup.find(title='Категория:Социологи по алфавиту')['href']

        # constructing the full link
        full_page_link = 'https://ru.wikipedia.org' + part_page_link

        return full_page_link

    else:
        return 'Connection error'
