from bs4 import BeautifulSoup as bs
from modules import links_constructor
from modules import session_generator


def run():
    links_arr = links_constructor.run()
    ages_arr = []

    for link in links_arr:

        # generation a new session
        request = session_generator.run(link)

        if request.status_code == 200:

            # getting day, month, year of birthday from a right block (biography)
            soup = bs(request.content, 'html.parser')

            # handling of index errors
            try:
                age = soup\
                    .find_all('span', attrs={'class', 'nowrap'})[0]\
                    .text
            except IndexError:
                pass

            ages_arr.append(age)

        else:
            return 'Connection error'

    # getting the result
    return ages_arr
