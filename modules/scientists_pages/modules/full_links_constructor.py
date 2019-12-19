from modules.scientists_pages.modules.data import scientists_pages


def run():
    links_arr = scientists_pages.show()

    full_links = []
    scientists_full_links = open('modules/data/scientists_full_links.txt', 'a')

    for link in links_arr:
        if link[0] == '/':
            link = 'https://ru.wikipedia.org' + link
            full_links.append(link)
            print(link)

    scientists_full_links.write(str(full_links))

    return full_links
