from modules.sciences_pages.modules import links_targets_generator


def run():

    links_targets = links_targets_generator.run()
    link_start = 'https://ru.wikipedia.org/wiki/Категория:'
    link_end = '_по_алфавиту'
    full_links = []

    for link_target in links_targets:
        full_link = link_start + link_target + link_end
        full_links.append(full_link)

    return full_links
