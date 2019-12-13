def run():

    links_ends = []

    formal_sciences = ['логики', 'математики', 'информатики', 'статисты', 'статистики']
    social_sciences = ['антропологи', 'историки', 'социологи', 'правоведы', 'политологи', 'культурологи', 'экономики']
    humanitarian_sciences = ['лингвисты', 'психологи', 'литературоведы', 'искусствоведы', 'педагоги', 'этики',
                             'эстетики', 'журналисты', 'филологи', 'философы']
    natural_sciences = ['антропологи', 'астрономы', 'биологи', 'ветеринары', 'географы', 'геологи', 'медики',
                        'метеорологи', 'океанологи', 'физики', 'химики']

    for link_end in formal_sciences:
        links_ends.append(link_end)
    for link_end in social_sciences:
        links_ends.append(link_end)
    for link_end in humanitarian_sciences:
        links_ends.append(link_end)
    for link_end in natural_sciences:
        links_ends.append(link_end)

    return links_ends
