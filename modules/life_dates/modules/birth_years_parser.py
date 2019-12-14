from bs4 import BeautifulSoup as bs
from modules.scientists_pages.modules import full_links_constructor
from modules import session_generator


def run():

    # generation a new session
    links_arr = full_links_constructor.run()
    request = session_generator.run(links_arr[0])

    if request.status_code == 200:

        # getting day, month, year of birthday from a right block (biography)
        soup = bs(request.content, 'html.parser')

        birth_day_and_month = soup\
            .find_all(attrs={'class': 'plainlist'})[1]\
            .find('span', attrs={'class', 'no-wikidata'})\
            .find_all('a')[0]\
            .text

        birth_year = soup \
            .find_all(attrs={'class': 'plainlist'})[1]\
            .find('span', attrs={'class', 'no-wikidata'})\
            .find_all('a')[1]\
            .text

        # getting the result
        return birth_day_and_month + ' ' + birth_year

    else:
        return 'Connection error'
