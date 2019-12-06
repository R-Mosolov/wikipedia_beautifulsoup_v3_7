from bs4 import BeautifulSoup as bs
from modules import links_constructor
from modules import session_generator


def run():

    # generation a new session
    links_arr = links_constructor.run()
    life_duration_arr = []

    for link in links_arr:
        request = session_generator.run(link)

        if request.status_code == 200:

            # getting day, month, year of birthday from a right block (biography)
            soup = bs(request.content, 'html.parser')

            # handling of index errors
            life_duration = ''
            try:
                life_duration = soup\
                    .find_all('span', attrs={'class', 'nowrap'})[0]\
                    .text
            except IndexError:
                pass

            life_duration_arr.append(life_duration)

            # getting the result
            return life_duration_arr

        else:
            return 'Connection error'
