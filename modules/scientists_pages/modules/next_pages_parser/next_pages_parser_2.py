# Unfortunately, the project author didn't find a method for realization the function without "copy-paste". Sorry!
from modules.scientists_pages.modules import next_page_searcher


def run():
    # journalists
    journalists__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Журналисты_по_алфавиту'
    journalists__page_2 = next_page_searcher.run(journalists__page_1, 'Журналисты', 0)
    journalists__page_3 = next_page_searcher.run(journalists__page_2, 'Журналисты')
    journalists__page_4 = next_page_searcher.run(journalists__page_3, 'Журналисты')
    journalists__page_5 = next_page_searcher.run(journalists__page_4, 'Журналисты')
    journalists__page_6 = next_page_searcher.run(journalists__page_5, 'Журналисты')
    journalists__page_7 = next_page_searcher.run(journalists__page_6, 'Журналисты')
    journalists__page_8 = next_page_searcher.run(journalists__page_7, 'Журналисты')
    journalists__page_9 = next_page_searcher.run(journalists__page_8, 'Журналисты')
    journalists__page_10 = next_page_searcher.run(journalists__page_9, 'Журналисты')
    journalists__page_11 = next_page_searcher.run(journalists__page_10, 'Журналисты')
    journalists__page_12 = next_page_searcher.run(journalists__page_11, 'Журналисты')
    journalists__page_13 = next_page_searcher.run(journalists__page_12, 'Журналисты')
    journalists__page_14 = next_page_searcher.run(journalists__page_13, 'Журналисты')
    journalists__page_15 = next_page_searcher.run(journalists__page_14, 'Журналисты')
    journalists__page_16 = next_page_searcher.run(journalists__page_15, 'Журналисты')
    journalists__page_17 = next_page_searcher.run(journalists__page_16, 'Журналисты')
    journalists__page_18 = next_page_searcher.run(journalists__page_17, 'Журналисты')
    journalists__page_19 = next_page_searcher.run(journalists__page_18, 'Журналисты')
    journalists__page_20 = next_page_searcher.run(journalists__page_19, 'Журналисты')
    journalists__page_21 = next_page_searcher.run(journalists__page_20, 'Журналисты')
    journalists__page_22 = next_page_searcher.run(journalists__page_21, 'Журналисты')
    journalists__page_23 = next_page_searcher.run(journalists__page_22, 'Журналисты')

    # philologists
    philologists__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Филологи_по_алфавиту'
    philologists__page_2 = next_page_searcher.run(philologists__page_1, 'Филологи', 0)
    philologists__page_3 = next_page_searcher.run(philologists__page_2, 'Филологи')
    philologists__page_4 = next_page_searcher.run(philologists__page_3, 'Филологи')

    # philosophers
    philosophers__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Философы_по_алфавиту'
    philosophers__page_2 = next_page_searcher.run(philosophers__page_1, 'Философы', 0)
    philosophers__page_3 = next_page_searcher.run(philosophers__page_2, 'Философы')
    philosophers__page_4 = next_page_searcher.run(philosophers__page_3, 'Философы')
    philosophers__page_5 = next_page_searcher.run(philosophers__page_4, 'Философы')
    philosophers__page_6 = next_page_searcher.run(philosophers__page_5, 'Философы')
    philosophers__page_7 = next_page_searcher.run(philosophers__page_6, 'Философы')
    philosophers__page_8 = next_page_searcher.run(philosophers__page_7, 'Философы')
    philosophers__page_9 = next_page_searcher.run(philosophers__page_8, 'Философы')
    philosophers__page_10 = next_page_searcher.run(philosophers__page_9, 'Философы')
    philosophers__page_11 = next_page_searcher.run(philosophers__page_10, 'Философы')

    # astronomers
    astronomers__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Астрономы_по_алфавиту'
    astronomers__page_2 = next_page_searcher.run(astronomers__page_1, 'Астрономы', 0)
    astronomers__page_3 = next_page_searcher.run(astronomers__page_2, 'Астрономы')
    astronomers__page_4 = next_page_searcher.run(astronomers__page_3, 'Астрономы')
    astronomers__page_5 = next_page_searcher.run(astronomers__page_4, 'Астрономы')
    astronomers__page_6 = next_page_searcher.run(astronomers__page_5, 'Астрономы')
    astronomers__page_7 = next_page_searcher.run(astronomers__page_6, 'Астрономы')
    astronomers__page_8 = next_page_searcher.run(astronomers__page_7, 'Астрономы')

    # biologists
    biologists__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Биологи_по_алфавиту'
    biologists__page_2 = next_page_searcher.run(biologists__page_1, 'Биологи', 0)

    # veterinarians
    veterinarians__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Ветеринары_по_алфавиту'

    # geographers
    geographers__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Географы_по_алфавиту'
    geographers__page_2 = next_page_searcher.run(geographers__page_1, 'Географы', 0)

    # geologist
    geologist__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Геологи_по_алфавиту'
    geologist__page_2 = next_page_searcher.run(geologist__page_1, 'Геологи', 0)
    geologist__page_3 = next_page_searcher.run(geologist__page_2, 'Геологи')
    geologist__page_4 = next_page_searcher.run(geologist__page_3, 'Геологи')

    # medics
    medics__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Медики_по_алфавиту'
    medics__page_2 = next_page_searcher.run(medics__page_1, 'Медики', 0)
    medics__page_3 = next_page_searcher.run(medics__page_2, 'Медики')
    medics__page_4 = next_page_searcher.run(medics__page_3, 'Медики')
    medics__page_5 = next_page_searcher.run(medics__page_4, 'Медики')
    medics__page_6 = next_page_searcher.run(medics__page_5, 'Медики')
    medics__page_7 = next_page_searcher.run(medics__page_6, 'Медики')
    medics__page_8 = next_page_searcher.run(medics__page_7, 'Медики')
    medics__page_9 = next_page_searcher.run(medics__page_8, 'Медики')
    medics__page_10 = next_page_searcher.run(medics__page_9, 'Медики')

    # doctors
    doctors__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Врачи_по_алфавиту'
    doctors__page_2 = next_page_searcher.run(doctors__page_1, 'Врачи', 0)
    doctors__page_3 = next_page_searcher.run(doctors__page_2, 'Врачи')
    doctors__page_4 = next_page_searcher.run(doctors__page_3, 'Врачи')
    doctors__page_5 = next_page_searcher.run(doctors__page_4, 'Врачи')

    # meteorologists
    meteorologists__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Метеорологи_по_алфавиту'

    # oceanographers
    oceanographers__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Океанографы_по_алфавиту'

    # physicists
    physicists__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Физики_по_алфавиту'
    physicists__page_2 = next_page_searcher.run(physicists__page_1, 'Физики', 0)
    physicists__page_3 = next_page_searcher.run(physicists__page_2, 'Физики')
    physicists__page_4 = next_page_searcher.run(physicists__page_3, 'Физики')
    physicists__page_5 = next_page_searcher.run(physicists__page_4, 'Физики')
    physicists__page_6 = next_page_searcher.run(physicists__page_5, 'Физики')
    physicists__page_7 = next_page_searcher.run(physicists__page_6, 'Физики')
    physicists__page_8 = next_page_searcher.run(physicists__page_7, 'Физики')
    physicists__page_9 = next_page_searcher.run(physicists__page_8, 'Физики')
    physicists__page_10 = next_page_searcher.run(physicists__page_9, 'Физики')

    # chemists
    chemists__page_1 = 'https://ru.wikipedia.org/wiki/Категория:Химики_по_алфавиту'
    chemists__page_2 = next_page_searcher.run(chemists__page_1, 'Химики', 0)
    chemists__page_3 = next_page_searcher.run(chemists__page_2, 'Химики')
    chemists__page_4 = next_page_searcher.run(chemists__page_3, 'Химики')
    chemists__page_5 = next_page_searcher.run(chemists__page_4, 'Химики')
    chemists__page_6 = next_page_searcher.run(chemists__page_5, 'Химики')

    return [['Журналисты: ' + journalists__page_1, journalists__page_2, journalists__page_3, journalists__page_4,
             journalists__page_5, journalists__page_6, journalists__page_7, journalists__page_8, journalists__page_9,
             journalists__page_10, journalists__page_11, journalists__page_12, journalists__page_13,
             journalists__page_14, journalists__page_15, journalists__page_16, journalists__page_17,
             journalists__page_18, journalists__page_19, journalists__page_20, journalists__page_21,
             journalists__page_22, journalists__page_23],
            ['Филологи: ' + philologists__page_1, philologists__page_2, philologists__page_3, philologists__page_4],
            ['Философы: ' + philosophers__page_1, philosophers__page_2, philosophers__page_3, philosophers__page_4,
             philosophers__page_5, philosophers__page_6, philosophers__page_7, philosophers__page_8,
             philosophers__page_9, philosophers__page_10, philosophers__page_11],
            ['Астрономы: ' + astronomers__page_1, astronomers__page_2, astronomers__page_3, astronomers__page_4,
             astronomers__page_5, astronomers__page_6, astronomers__page_7, astronomers__page_8],
            ['Биологи: ' + biologists__page_1, biologists__page_2],
            ['Ветеринары: ' + veterinarians__page_1],
            ['Географы: ' + geographers__page_1, geographers__page_2],
            ['Геологи: ' + geologist__page_1, geologist__page_2, geologist__page_3, geologist__page_4],
            ['Медики: ' + medics__page_1, medics__page_2, medics__page_3, medics__page_4, medics__page_5,
             medics__page_6, medics__page_7, medics__page_8, medics__page_9, medics__page_10],
            ['Врачи: ' + doctors__page_1, doctors__page_2, doctors__page_3, doctors__page_4, doctors__page_5],
            ['Метеорологи: ' + meteorologists__page_1],
            ['Океанографы: ' + oceanographers__page_1],
            ['Физики: ' + physicists__page_1, physicists__page_2, physicists__page_3, physicists__page_4,
             physicists__page_5, physicists__page_6, physicists__page_7, physicists__page_8, physicists__page_9,
             physicists__page_10],
            ['Химики: ' + chemists__page_1, chemists__page_2, chemists__page_3, chemists__page_4, chemists__page_5,
             chemists__page_6]]
