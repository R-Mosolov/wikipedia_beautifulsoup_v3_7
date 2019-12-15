from modules.scientists_pages.modules.data.scientists_pagination_2 import scientists_pagination
from modules.scientists_pages.modules import links_parts_parser


def run():
    all_scientists_links = []

    for link in scientists_pagination:
        parsed_link = links_parts_parser.run(link)
        all_scientists_links.append(parsed_link)
        print('\n\n\n' + str(all_scientists_links))
        print('\n' + str(len(all_scientists_links)))

    return all_scientists_links
