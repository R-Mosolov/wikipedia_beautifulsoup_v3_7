from bs4 import BeautifulSoup as bs
from modules.base_modules import session_generator


def get_next_page(link, scientist_type, following_page=1):
    # generation a new session
    request = session_generator.get_session(link)

    if request.status_code != 200:
        return None

    # getting the part link
    soup = bs(request.content, 'lxml').find_all(title='Категория:' + scientist_type + ' по алфавиту')

    if soup == []:
        return None

    attributes = soup[following_page]

    if attributes.next_element == 'Предыдущая страница':
        return None
    else:
        part_page_link = attributes['href']
        return 'https://ru.wikipedia.org' + part_page_link
