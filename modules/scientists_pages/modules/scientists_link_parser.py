from bs4 import BeautifulSoup as bs
from modules import session_generator


def get_scientists_links(link):
    # generation a new session
    request = session_generator.get_session(link)

    if request.status_code != 200:
        return 'Connection error'

    # getting all unordered lists
    soup = bs(request.content, 'lxml')
    all_href = []

    # error handling
    try:
        all_a = soup.find('div', attrs={'class', 'mw-category'}).find_all('a')

        # extracting links
        for href in all_a:
            result = 'https://ru.wikipedia.org' + href['href']
            all_href.append(result)
    except AttributeError:
        pass

    print('Collecting scientists pages for {}:'.format(str(link)))
    print('Collected {} scientists pages.'.format(len(all_href)))
    return all_href
