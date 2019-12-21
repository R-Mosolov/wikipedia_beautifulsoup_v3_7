from modules.sciences_pages.modules import category_links_generator


def run():
    print('Запущен конструктор полных ссылок научных направлений:')
    print(str(category_links_generator.full_links()))
    print('Закончен конструктор полных ссылок научных направлений!\n')

    print('Запущено тестирование страниц научных направлений:')
    print(str(category_links_generator.get_working_links()))
    print('Закончено тестирование страниц научных направлений!\n')


