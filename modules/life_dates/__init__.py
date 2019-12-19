from modules.life_dates.modules import ages_parser
from modules.life_dates.modules.data import ages_arr
from modules.life_dates.modules import ages_handler
from modules.life_dates.modules import month_converter
from modules.life_dates.modules import birth_years_parser


def run():
    print('3.1. Запущен парсер возрастов:')
    print(str(ages_parser.run()))
    print('3.1. Завершен парсер возрастов!\n')

    # print('3.2. Запущен показ результата парсинга возрастов:')
    # print(str(ages_arr.show()))
    # print('3.2. Завершен показ результата парсинга возрастов!\n')
    #
    # print('3.3. Запущена обработка возрастов и их разделение на 3 основных типа:')
    # print(str(ages_handler.run()))
    # print('3.3. Завершена обработка возрастов и их разделение на 3 основных типа!\n')
    #
    # print('3.4. Описание операции:')
    # print(str(month_converter.run()))
    # print('3.4. Описание операции!\n')
    #
    # print('3.5. Описание операции:')
    # print(str(birth_years_parser.run()))
    # print('3.5. Описание операции!\n')


if __name__ == '__main__':
    run()
