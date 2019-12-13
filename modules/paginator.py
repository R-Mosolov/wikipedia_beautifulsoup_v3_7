from bs4 import BeautifulSoup as bs
from modules import session_generator


def run():
    # generation a new session
    request = session_generator.run('https://ru.wikipedia.org/wiki/Категория:Социологи_по_алфавиту')

    if request.status_code == 200:
        # getting all unordered lists
        soup = bs(request.content, 'lxml')
        next_page_link = soup.find(title='Категория:Социологи по алфавиту')['href']

        return next_page_link

    else:
        return 'Connection error'


print(run())
