import re
from datetime import datetime as dt, date


def get_age(birth_date: str, death_date: str):
    if birth_date is None:
        return None

    if death_date is None:
        death_date = str(date.today())

    try:
        birth_date = dt.strptime(birth_date, '%Y-%m-%d').date()
        death_date = dt.strptime(death_date, '%Y-%m-%d').date()
        will_be_birthday_this_year = (death_date.month, death_date.day) < (birth_date.month, birth_date.day)
        return death_date.year - birth_date.year - will_be_birthday_this_year
    except ValueError:
        # Working with years, if any of dates contains only year
        birth_date = int(re.search(r'\d{3,4}', str(birth_date)).group(0))
        death_date = int(re.search(r'\d{3,4}', str(death_date)).group(0))

        # returning absolute difference, because has scientists before our era
        return int(abs(death_date - birth_date))
