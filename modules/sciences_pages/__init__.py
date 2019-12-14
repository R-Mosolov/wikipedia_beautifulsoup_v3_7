from modules.sciences_pages.modules import links_targets_generator
from modules.sciences_pages.modules import full_links_generator
from modules.sciences_pages.modules import links_quality_tester


def run():
    print('Запущен парсер частей ссылок научных направлений:')
    print(str(links_targets_generator.run()))
    print('Закончен парсер частей ссылок научных направлений!\n')

    print('Запущен конструктор полных ссылок научных направлений:')
    print(str(full_links_generator.run()))
    print('Закончен конструктор полных ссылок научных направлений!\n')

    print('Запущено тестирование страниц научных направлений:')
    print(str(links_quality_tester.run()))
    print('Закончено тестирование страниц научных направлений!\n')


if __name__ == '__main__':
    run()
