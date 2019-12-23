from modules.scientists_pages import next_page_searcher
from modules.base_modules.results_writers import write_scientists_pages
from modules.scientists_pages.scientists_link_parser import get_scientists_links
from modules.scientists_pages.scientists_category_parser import get_all_category_pages
from modules.sciences_pages.category_links_generator import get_working_links
from modules.sciences_pages.category_links_generator import get_scientist_type


def run():
    base_links = get_working_links()

    for science_link in base_links:
        science = get_scientist_type(science_link)
        print(science)

        print('Запущен парсер оглавлений:')
        category_pages = get_all_category_pages(science_link)
        print('Закончен парсинг оглавлений!\n')

        print('Запущен парсер ссылок всех страниц ученых:')
        scientists_links = []
        for page in category_pages:
            scientists_links += get_scientists_links(page.strip('\n'))
        print('Закончен парсер ссылок всех страниц ученых!\n')

        print('Запущено сохранение ссылок всех страниц ученых:')
        write_scientists_pages(scientists_links, science)
        print('Закончено сохранение ссылок всех страниц ученых!\n')
