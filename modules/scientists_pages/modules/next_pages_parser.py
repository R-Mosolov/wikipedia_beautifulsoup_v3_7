# Unfortunately, I didn't find a method for realization the function without "copy-paste". Sorry!
from modules.scientists_pages.modules import next_page_searcher


def run():
    # logics
    logics__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Логики_по_алфавиту'

    # mathematics
    mathematics__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Математики_по_алфавиту'
    mathematics__page_2 = next_page_searcher.run(mathematics__page_1, 'Математики', 0)
    mathematics__page_3 = next_page_searcher.run(mathematics__page_2, 'Математики')
    mathematics__page_4 = next_page_searcher.run(mathematics__page_3, 'Математики')
    mathematics__page_5 = next_page_searcher.run(mathematics__page_4, 'Математики')
    mathematics__page_6 = next_page_searcher.run(mathematics__page_5, 'Математики')
    mathematics__page_7 = next_page_searcher.run(mathematics__page_6, 'Математики')
    mathematics__page_8 = next_page_searcher.run(mathematics__page_7, 'Математики')
    mathematics__page_9 = next_page_searcher.run(mathematics__page_8, 'Математики')
    mathematics__page_10 = next_page_searcher.run(mathematics__page_9, 'Математики')
    mathematics__page_11 = next_page_searcher.run(mathematics__page_10, 'Математики')
    mathematics__page_12 = next_page_searcher.run(mathematics__page_11, 'Математики')
    mathematics__page_13 = next_page_searcher.run(mathematics__page_12, 'Математики')
    mathematics__page_14 = next_page_searcher.run(mathematics__page_13, 'Математики')

    # statistics
    statistics__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Статистики_по_алфавиту'

    # anthropologists
    anthropologists__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Антропологи_по_алфавиту'

    # historians
    historians__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Историки_по_алфавиту'
    historians__page_2 = next_page_searcher.run(historians__page_1, 'Историки', 0)
    historians__page_3 = next_page_searcher.run(historians__page_2, 'Историки')
    historians__page_4 = next_page_searcher.run(historians__page_3, 'Историки')
    historians__page_5 = next_page_searcher.run(historians__page_4, 'Историки')
    historians__page_6 = next_page_searcher.run(historians__page_5, 'Историки')
    historians__page_7 = next_page_searcher.run(historians__page_6, 'Историки')
    historians__page_8 = next_page_searcher.run(historians__page_7, 'Историки')
    historians__page_9 = next_page_searcher.run(historians__page_8, 'Историки')
    historians__page_10 = next_page_searcher.run(historians__page_9, 'Историки')
    historians__page_11 = next_page_searcher.run(historians__page_10, 'Историки')
    historians__page_12 = next_page_searcher.run(historians__page_11, 'Историки')
    historians__page_13 = next_page_searcher.run(historians__page_12, 'Историки')
    historians__page_14 = next_page_searcher.run(historians__page_13, 'Историки')
    historians__page_15 = next_page_searcher.run(historians__page_14, 'Историки')
    historians__page_16 = next_page_searcher.run(historians__page_15, 'Историки')
    historians__page_17 = next_page_searcher.run(historians__page_16, 'Историки')
    historians__page_18 = next_page_searcher.run(historians__page_17, 'Историки')
    historians__page_19 = next_page_searcher.run(historians__page_18, 'Историки')
    historians__page_20 = next_page_searcher.run(historians__page_19, 'Историки')

    # sociologists
    sociologists__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Социологи_по_алфавиту'
    sociologists__page_2 = next_page_searcher.run(sociologists__page_1, 'Социологи', 0)
    sociologists__page_3 = next_page_searcher.run(sociologists__page_2, 'Социологи')
    sociologists__page_4 = next_page_searcher.run(sociologists__page_3, 'Социологи')

    # lawyers
    lawyers__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Правоведы_по_алфавиту'

    # political_scientists
    political_scientists__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Политологи_по_алфавиту'
    political_scientists__page_2 = next_page_searcher.run(political_scientists__page_1, 'Политологи')

    # economists
    economists__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Экономисты_по_алфавиту'
    economists__page_2 = next_page_searcher.run(economists__page_1, 'Экономисты', 0)
    economists__page_3 = next_page_searcher.run(economists__page_2, 'Экономисты')
    economists__page_4 = next_page_searcher.run(economists__page_3, 'Экономисты')
    economists__page_5 = next_page_searcher.run(economists__page_4, 'Экономисты')
    economists__page_6 = next_page_searcher.run(economists__page_5, 'Экономисты')
    economists__page_7 = next_page_searcher.run(economists__page_6, 'Экономисты')
    economists__page_8 = next_page_searcher.run(economists__page_7, 'Экономисты')
    economists__page_9 = next_page_searcher.run(economists__page_8, 'Экономисты')
    economists__page_10 = next_page_searcher.run(economists__page_9, 'Экономисты')
    economists__page_11 = next_page_searcher.run(economists__page_10, 'Экономисты')
    economists__page_12 = next_page_searcher.run(economists__page_11, 'Экономисты')
    economists__page_13 = next_page_searcher.run(economists__page_12, 'Экономисты')
    economists__page_14 = next_page_searcher.run(economists__page_13, 'Экономисты')
    economists__page_15 = next_page_searcher.run(economists__page_14, 'Экономисты')

    # linguists
    linguists__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Лингвисты_по_алфавиту'
    linguists__page_2 = next_page_searcher.run(linguists__page_1, 'Лингвисты')

    # psychologists
    psychologists__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Психологи_по_алфавиту'
    psychologists__page_2 = next_page_searcher.run(psychologists__page_1, 'Психологи')
    psychologists__page_3 = next_page_searcher.run(psychologists__page_2, 'Психологи')

    return [['Логики: ' + logics__page_1],
            ['Математики: ' + mathematics__page_1, mathematics__page_2, mathematics__page_3, mathematics__page_4,
             mathematics__page_5, mathematics__page_6, mathematics__page_7, mathematics__page_8, mathematics__page_9,
             mathematics__page_10, mathematics__page_11, mathematics__page_12, mathematics__page_13,
             mathematics__page_14],
            ['Статистики: ' + statistics__page_1],
            ['Антропологи: ' + anthropologists__page_1],
            ['Историки: ' + historians__page_1, historians__page_2, historians__page_3, historians__page_4,
             historians__page_5, historians__page_6, historians__page_7, historians__page_8, historians__page_9,
             historians__page_10, historians__page_11, historians__page_12, historians__page_13, historians__page_14,
             historians__page_15, historians__page_16, historians__page_17, historians__page_18, historians__page_19,
             historians__page_20],
            ['Социологи: ' + sociologists__page_1, sociologists__page_2, sociologists__page_3, sociologists__page_4],
            ['Правоведы: ' + lawyers__page_1],
            ['Политологи: ' + political_scientists__page_1 + political_scientists__page_2],
            ['Экономисты: ' + economists__page_1, economists__page_2, economists__page_3, economists__page_4,
             economists__page_5, economists__page_6, economists__page_7, economists__page_8, economists__page_9,
             economists__page_10, economists__page_11, economists__page_12, economists__page_13, economists__page_14,
             economists__page_15],
            ['Лингвисты: ' + linguists__page_1, linguists__page_2],
            ['Психологи: ' + psychologists__page_1, psychologists__page_2, psychologists__page_3]]
