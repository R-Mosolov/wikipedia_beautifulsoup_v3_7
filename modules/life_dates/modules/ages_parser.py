from bs4 import BeautifulSoup as bs
from modules.scientists_pages.modules import full_links_constructor
from modules import session_generator


def run():
    request = session_generator.run('https://ru.wikipedia.org/wiki/Категория:Социологи_по_алфавиту')
    links_arr = full_links_constructor.run()
    ages_arr = []

    if request.status_code == 200:
        for link in links_arr:
            request = session_generator.run(link)
            soup = bs(request.content, 'lxml')

            try:
                age = soup\
                    .find_all('span', attrs={'class', 'nowrap'})[0]\
                    .text
                print(age)
            except IndexError:
                pass

            ages_arr.append(age)

    else:
        return 'Connection error'
