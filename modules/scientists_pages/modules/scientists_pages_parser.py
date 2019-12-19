from modules.scientists_pages.modules.data.scientists_pagination_2 import scientists_pagination
from modules.scientists_pages.modules import links_parts_parser
from openpyxl import Workbook

wb = Workbook()
ws = wb.active


def run():
    all_scientists_links = []

    for link in scientists_pagination:
        parsed_link = links_parts_parser.run(link)
        all_scientists_links.append(parsed_link)

        # recording the result in an excel file
        ws['A' + str(len(all_scientists_links))] = str(parsed_link) + ', '
        wb.save("modules/data/scientists_pages.xlsx")

        # showing the result for debugging
        print('\n\n\n' + str(all_scientists_links))
        print('\n' + str(len(all_scientists_links)))

    return all_scientists_links
