from bs4 import BeautifulSoup as bs
from modules import session_generator
import re
import datetime as dt
import pandas as pd


def get_month_by_name(month_name):
    months = {
        'января': '01',
        'февраля': '02',
        'марта': '03',
        'апреля': '04',
        'мая': '05',
        'июня': '06',
        'июля': '07',
        'августа': '08',
        'сентября': '09',
        'октября': '10',
        'ноября': '11',
        'декабря': '12'
    }
    return months[month_name]


def select_date_pattern(date):
    patterns = [r'\d{4}-\d{2}-\d{2}', r'\d{2} \w+ \d{4}', r'\d{4}', r'\d{3}']
    for pattern in patterns:
        date_search = re.search(pattern, date)
        if date_search is not None:
            return pattern

    print('Date pattern not found!')
    return None


def prettify_date(date):
    """
    Change dates like 26 апреля 1889 to 1889-04-26.
    """

    if date is None:
        return None

    pattern = select_date_pattern(date)
    if pattern != r'\d{2} \w+ \d{4}':
        return date

    search = re.search(r'(\d{2}) (\w+) (\d{4})', date)
    day = search.group(1)  # (\d{2})
    month = get_month_by_name(search.group(2))  # (\w+)
    year = search.group(3)  # (\d{4})
    return '{}-{}-{}'.format(year, month, day)


def prettify_text(text):
    if text is None:
        return None

    result = re.sub(r'\s+', ' ', re.sub(r'\[.*\]', '', text)).strip()
    return result[:1].upper() + result[1:]


def select_best_date(date):
    """
    Selecting best date type in response Wikipedia.
    """
    if date is None:
        return None

    pattern = select_date_pattern(date)
    return re.search(pattern, date).group(0)


def get_age(birth_date, death_date):
    if death_date is None:
        death_date = str(dt.date.today())

    # Working with years, if any of dates contain only year
    is_year_mode = any([re.search(r'^\d{3,4}$', x) for x in [birth_date, death_date]])
    if is_year_mode:
        birth_date = int(re.search(r'\d{3,4}', str(birth_date)).group(0))
        death_date = int(re.search(r'\d{3,4}', str(death_date)).group(0))
        return abs(death_date - birth_date)

    birth_date = dt.datetime.strptime(birth_date, '%Y-%m-%d').date()
    death_date = dt.datetime.strptime(death_date, '%Y-%m-%d').date()
    return death_date.year - birth_date.year - ((death_date.month, death_date.day) < (birth_date.month, birth_date.day))


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


def delete_duplicates(string):
    if string is None:
        return None

    uniques = set(string.split(' '))
    return ' '.join(uniques)


def test(link):
    request = session_generator.get_session(link)
    soup = bs(request.content, 'html.parser')

    #print(soup.prettify())

    birth_date = prettify_date(select_best_date(find_object(soup, 'P569')))
    death_date = prettify_date(select_best_date(find_object(soup, 'P570')))
    age = get_age(birth_date, death_date)
    print(birth_date, '|', death_date, '|', age)

    country = prettify_text(delete_duplicates(find_object(soup, 'P27')))
    birth_place = prettify_text(delete_duplicates(find_object(soup, 'P19')))
    birth_place = country if birth_place is None else birth_place

    death_place = prettify_text(delete_duplicates(find_object(soup, 'P20')))
    death_place = birth_place if death_date is not None and death_place is None else death_place
    print(birth_place, '|', death_place)

    name = prettify_text(soup.find(attrs='infobox-above').text)
    print(name)

    result = {
        'name': name,
        'birth_place': birth_place,
        'death_place': death_place,
        'birth_date': birth_date,
        'death_date': death_date
    }

    #print(pd.DataFrame([result, result]))
    #return result


#file = open('../../scientists_pages/modules/data/scientists_pages_логики.txt', 'r')
#scientist_type = next(file)
#print(scientist_type)
#for l in file:
#    link = l.strip('\n')
#    print(link)
#    test(link)
#file.close()


test('https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%B8%D0%BF%D0%BA%D0%B5,_%D0%A1%D0%BE%D0%BB')