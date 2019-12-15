from bs4 import BeautifulSoup as bs
from modules import session_generator


def run(link):
    # generation a new session
    request = session_generator.run(link)

    if request.status_code == 200:

        # getting all unordered lists
        soup = bs(request.content, 'lxml')
        all_href = []

        # error handling
        try:
            all_a = soup \
                .find('div', attrs={'class', 'mw-category'}) \
                .find_all('a')

            # extracting links parts
            for href in all_a:
                result = href['href']
                all_href.append(result)

        except AttributeError:
            pass

        return all_href

    else:
        return 'Connection error'
