from bs4 import BeautifulSoup as bs
from modules import session_generator


def run(link, sciencetist_type, following_page=1):
    # generation a new session
    request = session_generator.run(link)

    if request.status_code == 200:

        # getting the part link
        soup = bs(request.content, 'lxml')
        part_page_link = soup.find_all(title='Категория:' + sciencetist_type + ' по алфавиту')[following_page]['href']

        # constructing the full link
        full_page_link = 'https://ru.wikipedia.org' + part_page_link

        return full_page_link

    else:
        return 'Connection error'
