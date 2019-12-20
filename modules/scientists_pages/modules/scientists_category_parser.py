from modules.scientists_pages.modules import next_page_searcher


def get_next_pages(link, scientist_type):
    next_page = next_page_searcher.get_next_page(link, scientist_type)
    if next_page is not None:
        # Use recursion for getting list of links
        return [next_page] + get_next_pages(next_page, scientist_type)
    else:
        # Get whole links except last element, because last is None everything
        return [next_page][:-1]


def get_all_category_pages(categories):
    result = []

    sort_type = '_по_алфавиту'

    for scientist_type in categories:
        print('Collecting pages for {}:'.format(scientist_type))
        base_link = 'https://ru.wikipedia.org/wiki/Категория:' + scientist_type + sort_type
        pages = [base_link] + get_next_pages(base_link, scientist_type)
        print('Collected {} pages.'.format(len(pages)))
        print()
        result += pages

    return result
