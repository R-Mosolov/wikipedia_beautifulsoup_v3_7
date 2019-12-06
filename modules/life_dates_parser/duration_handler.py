from modules.life_dates_parser.ages_arr import ages


def run():
    ages_in_brackets = []
    not_full_ages = []
    not_ages = []

    for age in ages:
        age_in_bracket = len(age.split()) == 2
        not_full_age = len(age.split()) == 3

        if age_in_bracket:
            ages_in_brackets.append(age)

        if not_full_age:
            not_full_ages.append(age)

        if not age_in_bracket and not not_full_age:
            not_ages.append(age)

    print(len(ages_in_brackets))
    print(len(not_full_ages))
    print(len(not_ages))