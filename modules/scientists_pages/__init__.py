from modules.scientists_pages.modules import links_parts_parser
from modules.scientists_pages.modules import full_links_constructor
from modules.scientists_pages.modules import next_page_searcher
from modules.scientists_pages.modules.next_pages_parser import next_pages_parser_1
from modules.scientists_pages.modules.next_pages_parser import next_pages_parser_2
from modules.scientists_pages.modules import next_page_centralizer
from modules.scientists_pages.modules import scientists_pages_parser


def run():
    # print('Запущен парсер частей ссылок ученых:')
    # print(str(links_parts_parser.run()))
    # print('Закончен парсер частей ссылок ученых!\n')
    #
    # print('Запущен конструктор полных ссылок ученых:')
    # print(str(full_links_constructor.run()))
    # print('Закончен конструктор полных ссылок ученых!\n')
    #
    # print('Запущен поиск ссылки следующей страницы ученых:')
    # print(str(next_page_searcher.run()))
    # print('Закончен поиск ссылки следующей страницы ученых!\n')
    #
    # print('Запущен парсер ссылок всех страниц ученых:')
    # print(str(next_pages_parser_1.run()))
    # print('Закончен парсер ссылок всех страниц ученых!\n')
    #
    # print('Запущен парсер ссылок всех страниц ученых:')
    # print(str(next_pages_parser_2.run()))
    # print('Закончен парсер ссылок всех страниц ученых!\n')
    #
    # print('Запущена централизация ссылок в одном массиве:')
    # print(str(next_page_centralizer.run()))
    # print('Закончена централизация ссылок в одном массиве!\n')
    #
    # print('Запущен парсер страниц ученых:')
    # print(str(scientists_pages_parser.run()))
    # print('Закончен парсер страниц ученых!\n')
    #
    print('Запущен конструктор полных ссылок ученых:')
    print(str(full_links_constructor.run()))
    print('Закончен конструктор полных ссылок ученых!\n')


if __name__ == '__main__':
    run()
