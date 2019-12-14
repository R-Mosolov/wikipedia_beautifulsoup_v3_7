from modules.scientists_pages.modules import links_parts_parser


def run():
    links_arr = links_parts_parser.run()
    full_links = []

    for link in links_arr:
        if link[0] == '/':
            link = 'https://ru.wikipedia.org' + link
            full_links.append(link)

    return full_links
