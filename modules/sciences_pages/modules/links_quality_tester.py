from modules.sciences_pages.modules import full_links_generator
from modules import session_generator


def run():

    full_links = full_links_generator.run()
    work_links = []
    not_work_links = []

    for link in full_links:
        request = session_generator.run(link)

        if request.status_code == 200:
            work_links.append('Good connection')
        else:
            not_work_links.append(['Connection error', link])

    return [work_links, not_work_links]
