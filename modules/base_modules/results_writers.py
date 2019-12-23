import os


def write_scientists_pages(links, category):
    script_dir = os.path.dirname(__file__)
    path = os.path.relpath(os.getcwd(), script_dir)
    file = open(path + '/data/scientists_pages_' + category.lower() + '.txt', 'w')
    file.write(category + '\n')
    for link in links:
        file.write(link + '\n')

    file.close()
