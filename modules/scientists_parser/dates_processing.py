import re
from datetime import datetime as dt

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

    for month in months:
        try:
            return months[re.search(re.compile('.*' + month_name + '.*'), month).group(0)]
        except AttributeError:
            continue


def select_date_pattern(date):
    patterns = [r'\d{4}-\d{2}-\d{2}', r'\d{2} \w+ \d{4}', r'\d{4}', r'\d{3}']
    for pattern in patterns:
        date_search = re.search(pattern, date)
        if date_search is not None:
            return pattern

    return None


def select_best_date(date):
    """
    Selecting best date type in response Wikipedia.
    """
    if date is None:
        return None

    pattern = select_date_pattern(date)
    if pattern is None:
        return None
    return re.search(pattern, date).group(0)


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
    day = search.group(1)                               # (\d{2})
    month = get_month_by_name(search.group(2))          # (\w+)
    year = search.group(3)                              # (\d{4})

    result = '{}-{}-{}'.format(year, month, day)
    try:
        return dt.strptime(result, '%Y-%m-%d').date().__str__()
    except TypeError:
        return re.search(r'\d{3,4}', str(result)).group(0)
    except ValueError:
        return re.search(r'\d{3,4}', str(result)).group(0)
