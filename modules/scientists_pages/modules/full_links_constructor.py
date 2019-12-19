from modules.scientists_pages.modules.data import scientists_pages
from openpyxl import Workbook

wb = Workbook()
ws = wb.active


def run():
    links_arr = scientists_pages.show()
    full_links = []

    for link in links_arr:
        if link[0] == '/':
            link = 'https://ru.wikipedia.org' + link
            full_links.append(link)

            # recording the result in an excel file
            ws['A' + str(len(full_links))] = str(link) + ', '
            wb.save("modules/data/scientists_full_links.xlsx")

            print(link)

    return full_links
