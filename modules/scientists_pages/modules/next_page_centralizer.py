from modules.scientists_pages.modules.next_pages_parser import next_pages_parser_1
from modules.scientists_pages.modules.next_pages_parser import next_pages_parser_2


def run():
    arr_1 = next_pages_parser_1.run()
    arr_2 = next_pages_parser_2.run()

    summary_arr = arr_1 + arr_2
    only_links = []

    for arr in summary_arr:
        arr.pop(0)
        for item in arr:
            only_links.append(item)

    return only_links
