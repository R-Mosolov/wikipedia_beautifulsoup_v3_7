from modules.life_dates_parser import duration_handler
import re


ages_in_brackets = duration_handler.run()[0]
not_full_ages = duration_handler.run()[1]
not_ages = duration_handler.run()[2]

ages_in_brackets__only_ages = []
not_full_ages__only_day = []
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


for age in not_full_ages:
    only_year = re.findall('\d\d\d\d', age)[0]
    not_full_ages__only_year.append(only_year)


print('Массив возрастов: \n' + str(ages_in_brackets__only_ages))
print('Массив дней рождения: \n' + str(not_full_ages__only_day))
print('Массив годов рождения: \n' + str(not_full_ages__only_year))
