from modules.scientists_pages import next_page_searcher
from modules.sciences_pages.category_links_generator import get_working_links
from modules.sciences_pages.category_links_generator import get_scientist_type


def get_next_pages(link, scientist_type):
    next_page = next_page_searcher.get_next_page(link, scientist_type)
    if next_page is not None:
        # Use recursion for getting list of links
        return [next_page] + get_next_pages(next_page, scientist_type)
    else:
        # Get whole links except last element, because last is None everything
        return [next_page][:-1]


def get_all_category_pages(base_links=get_working_links()):
    result = []

    for link in [base_links]:
        scientist_type = get_scientist_type(link)
        print('Collecting pages for {}:'.format(scientist_type))
        pages = [link] + get_next_pages(link, scientist_type)
        print('Collected {} pages.'.format(len(pages)))
        print()
        result += pages

    return result
