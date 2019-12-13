from modules import links_parser
from modules import links_constructor
from modules import next_page_definer

from modules.life_dates_parser import birth_year_parser
from modules.life_dates_parser import ages_parser
from modules.life_dates_parser import duration_handler

from modules.sciences_links_generator import links_targets_generator
from modules.sciences_links_generator import full_links_generator

# print(links_parser.run())
# print(links_constructor.run())
# print(next_page_definer.run())
# print(birth_year_parser.run())
# print(ages_parser.run())
# duration_handler.run()
# print(links_ends_generator.run())
print(full_links_generator.run())
