import re


def prettify_text(text):
    if text is None:
        return None

    result = re.sub(r'\s+', ' ', re.sub(r'\[.*\]', '', text)).strip()
    return result[:1].upper() + result[1:]


def delete_duplicates(string):
    if string is None:
        return None

    uniques = set(string.split(' '))
    return ' '.join(uniques)
