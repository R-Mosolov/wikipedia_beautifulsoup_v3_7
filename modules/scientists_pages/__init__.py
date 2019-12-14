from modules.scientists_pages.modules import links_parts_parser
from modules.scientists_pages.modules import full_links_constructor
from modules.scientists_pages.modules import next_page_searcher
from modules.scientists_pages.modules import next_pages_parser


def run():
    print('Запущен парсер частей ссылок ученых:')
    print(str(links_parts_parser.run()))
    print('Закончен парсер частей ссылок ученых!\n')

    print('Запущен конструктор полных ссылок ученых:')
    print(str(full_links_constructor.run()))
    print('Закончен конструктор полных ссылок ученых!\n')

    print('Запущен поиск ссылки следующей страницы ученых:')
    print(str(next_page_searcher.run()))
    print('Закончен поиск ссылки следующей страницы ученых!\n')

    print('Запущен парсер ссылок всех страниц ученых:')
    print(str(next_pages_parser.run()))
    print('Закончен парсер ссылок всех страниц ученых!\n')


if __name__ == '__main__':
    run()
