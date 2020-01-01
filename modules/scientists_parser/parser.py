from bs4 import BeautifulSoup as bs
from modules.base_modules import session_generator
import pandas as pd
from modules.scientists_parser.age_processing import *
from modules.scientists_parser.dates_processing import *
from modules.scientists_parser.text_processing import *


def find_object(soup_obj, wiki_property, sep=' '):
    """
    Find specific object from response via soup. Working with soup objects:
    - P569: birth date,
    - P570: death date,
    - P19: birth place,
    - P20: death place.
    """
    links = soup_obj.find('span', {'data-wikidata-property-id': wiki_property})

    obj = ''
    if links is not None:
        if len(links) == 1:
            obj += sep + links.text
            obj = obj.strip()
            return obj

        for link in links.findAll(re.compile(r'a|span')):
            obj += sep + link.text
            obj = obj.strip()

        return obj


def count_works(soup_obj):
    works = 0

    # Search list items in these categories
    work_types = re.compile(r'(работы|сочинения|произведения|труды|публикации|библиография)', re.IGNORECASE)
    links = soup_obj.find('span', {'class': 'mw-headline', 'id': work_types})
    if links is None:
        return works

    # Count all list items
    while True:
        links = links.findNext('ul')
        if links is None:
            break
        works += len(links.text.split('\n'))

        check = links.findNext('dl')
        if check is None:
            check = links.findNext('span', {'class': 'mw-headline'})
            if check is None:
                break
        if check.text in ('См. также', 'Литература', 'Ссылки', 'Награды', 'Примечания'):
            break
    return works


def parse_scientist_info(link, science):
    request = session_generator.get_session(link)
    soup = bs(request.content, 'html.scientists')
    print(link)

    birth_date = prettify_date(select_best_date(find_object(soup, 'P569')))
    death_date = prettify_date(select_best_date(find_object(soup, 'P570')))
    age = get_age(birth_date, death_date)
    #print('Birth date: {}, death date: {}, age: {}'.format(birth_date, death_date, age))

    country = prettify_text(delete_duplicates(find_object(soup, 'P27')))
    birth_place = prettify_text(delete_duplicates(find_object(soup, 'P19')))
    birth_place = country if birth_place is None else birth_place

    death_place = prettify_text(delete_duplicates(find_object(soup, 'P20')))
    death_place = birth_place if death_date is not None and death_place is None else death_place

    try:
        name = prettify_text(soup.find(attrs='infobox-above').text)
    except AttributeError:
        name = prettify_text(soup.find('h1', {'class': 'firstHeading', 'lang': 'ru'}).text)

    #print('Name: {}'.format(name))

    # Count number of works
    works = count_works(soup)
    #print(birth_place, '|', death_place)
    #print('Works:', works)

    result = {
        'science': science,
        'name': name,
        'birth_place': birth_place,
        'death_place': death_place,
        'birth_date': birth_date,
        'death_date': death_date,
        'age': age,
        'works': works,
        'link': link
    }
    return result


def parse_all_scientists(links, science):
    result = []
    for link in links:
        result.append(parse_scientist_info(link, science))
    return pd.DataFrame(result)
