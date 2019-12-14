from modules.life_dates.modules import ages_parser
from modules.life_dates.modules.data import ages_arr
from modules.life_dates.modules import ages_handler
from modules.life_dates.modules import month_converter
from modules.life_dates.modules import birth_years_parser


def run():
    print('Запущен парсер возрастов:')
    print(str(ages_parser.run()))
    print('Завершен парсер возрастов!\n')

    print('Запущен показ результата парсинга возрастов:')
    print(str(ages_arr.show()))
    print('Завершен показ результата парсинга возрастов!\n')

    print('Запущена обработка возрастов и их разделение на 3 основных типа:')
    print(str(ages_handler.run()))
    print('Завершена обработка возрастов и их разделение на 3 основных типа!\n')

    print('Описание операции:')
    print(str(month_converter.run()))
    print('Описание операции!\n')

    print('Описание операции:')
    print(str(birth_years_parser.run()))
    print('Описание операции!\n')


if __name__ == '__main__':
    run()
