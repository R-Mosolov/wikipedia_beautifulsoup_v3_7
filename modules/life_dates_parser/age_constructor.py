from modules.life_dates_parser import duration_handler
import re


ages_in_brackets = duration_handler.run()[0]
not_full_ages = duration_handler.run()[1]
not_ages = duration_handler.run()[2]

ages_in_brackets__only_ages = []
not_full_ages__only_day = []
not_full_ages__only_month = []
not_full_ages__only_year = []


for age in ages_in_brackets:
    try:
        only_age = re.findall('\d\d', age)[0]
    except IndexError:
        pass
    ages_in_brackets__only_ages.append(only_age)

for day in not_full_ages:
    only_day = re.findall('\d\d', day)[0]
    not_full_ages__only_day.append(only_day)

for month in not_full_ages:
    current_month = month.split()[1]

    if current_month == 'января':
        not_full_ages__only_month.append('01')
    if current_month == 'февраля':
        not_full_ages__only_month.append('02')
    if current_month == 'марта':
        not_full_ages__only_month.append('03')
    if current_month == 'апреля':
        not_full_ages__only_month.append('04')
    if current_month == 'мая':
        not_full_ages__only_month.append('05')
    if current_month == 'июня':
        not_full_ages__only_month.append('06')
    if current_month == 'июля':
        not_full_ages__only_month.append('07')
    if current_month == 'августа':
        not_full_ages__only_month.append('08')
    if current_month == 'сентября':
        not_full_ages__only_month.append('09')
    if current_month == 'октября':
        not_full_ages__only_month.append('10')
    if current_month == 'ноября':
        not_full_ages__only_month.append('11')
    if current_month == 'декабря':
        not_full_ages__only_month.append('12')

for age in not_full_ages:
    only_year = re.findall('\d\d\d\d', age)[0]
    not_full_ages__only_year.append(only_year)


print('Массив возрастов: \n' + str(ages_in_brackets__only_ages))
print('Массив дней рождения: \n' + str(not_full_ages__only_day))
print('Массив месяцев рождения: \n' + str(not_full_ages__only_month))
print('Массив годов рождения: \n' + str(not_full_ages__only_year))
