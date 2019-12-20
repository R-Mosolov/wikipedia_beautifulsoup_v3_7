from openpyxl import Workbook


def write_scientists_links(links):
    wb = Workbook()
    ws = wb.active

    for index in range(len(links)):
        # recording the result in an excel file
        ws['A' + str(index+1)] = str(links[index]) + ', '

    wb.save("modules/data/scientists_pages.xlsx")
    print('File with scientists links saved!')
