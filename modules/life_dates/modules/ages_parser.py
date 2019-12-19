from bs4 import BeautifulSoup as bs
from modules.scientists_pages.modules import full_links_constructor
from modules import session_generator


def run():
    request = session_generator.run('https://ru.wikipedia.org/wiki/Категория:Социологи_по_алфавиту')
    links_arr = full_links_constructor.run()

    ages_arr = []
    unsorted_ages = open('modules/data/unsorted_ages.txt', 'a')

    if request.status_code == 200:
        unsorted_ages.truncate(0)

        for link in links_arr:
            request = session_generator.run(link)
            soup = bs(request.content, 'lxml')

            try:
                age = soup \
                    .find('span', attrs={'class', 'nowrap'}) \
                    .text
                unsorted_ages.write(str("'" + age + "'" + ', '))
                print(age)
            except:
                pass

            ages_arr.append(age)

    else:
        return 'Connection error'
