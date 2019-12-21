from modules import session_generator
import re


def target_links():
    formal_sciences = ['логики', 'математики', 'статистики']
    social_sciences = ['антропологи', 'историки', 'социологи', 'правоведы', 'политологи', 'экономисты']
    humanitarian_sciences = ['лингвисты', 'психологи', 'литературоведы', 'искусствоведы', 'педагоги', 'журналисты',
                             'филологи', 'философы']
    natural_sciences = ['астрономы', 'биологи', 'ветеринары', 'географы', 'геологи', 'медики', 'врачи',
                        'метеорологи', 'океанографы', 'физики', 'химики']

    return formal_sciences + social_sciences + humanitarian_sciences + natural_sciences


def full_links():
    link_start = 'https://ru.wikipedia.org/wiki/Категория:'
    link_end = '_по_алфавиту'
    result = []

    for link_target in target_links():
        full_link = link_start + link_target + link_end
        result.append(full_link)

    return result


def get_scientist_type(link):
    search = re.search(r'.*Категория:(.*)_по_.*', link, re.IGNORECASE)
    try:
        scientist_type = search.group(1).capitalize()
        return scientist_type
    except AttributeError:
        print('Not found scientist type!')
        exit()


def get_working_links(cache=True):
    work_links = []

    if cache:
        file = open('../sciences_pages/data/category_links.txt', 'r+')
        work_links = [line.strip() for line in file.readlines() if line.strip() != '']

        if len(work_links) > 1:
            file.close()
            return work_links

    for link in full_links():
        request = session_generator.get_session(link)

        if request.status_code == 200:
            work_links.append(link)
            if cache:
                file.write(link + '\n')
    if cache:
        file.close()
    return work_links
