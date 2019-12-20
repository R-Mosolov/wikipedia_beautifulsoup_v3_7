from modules.scientists_pages.modules import next_page_searcher
from modules.scientists_pages.modules.scientists_links_writer import write_scientists_links
from modules.scientists_pages.modules.scientists_link_parser import get_scientists_links
from modules.scientists_pages.modules.scientists_category_parser import get_all_category_pages


def run():
    # Set all types of scientists
    scientist_types = [
        #'Математики',
        'Антропологи',
        #'Историки',
        #'Социологи',
        #'Лингвисты',
        #'Логики',
        #'Статистики',
        #'Правоведы',
        #'Политологи',
        #'Экономисты',
        #'Психологи',
        #'Литературоведы',
        #'Искусствоведы'
        #'Педагоги',
        #'Журналисты',
        #'Филологи',
        #'Философы',
        #'Астрономы',
        #'Биологи',
        #'Ветеринары',
        #'Географы',
        #'Геологи',
        #'Медики',
        #'Врачи',
        #'Океанографы',
        #'Физики',
        #'Химики'
    ]

    print('Запущен парсер оглавлений:')
    category_pages = get_all_category_pages(scientist_types)
    print('Закончен парсинг оглавлений!\n')


    print('Запущен парсер ссылок всех страниц ученых:')
    scientists_links = []
    for page in category_pages:
        scientists_links += get_scientists_links(page)
    print('Закончен парсер ссылок всех страниц ученых!\n')

    print('Запущено сохранение ссылок всех страниц ученых:')
    write_scientists_links(scientists_links)


if __name__ == '__main__':
    run()
