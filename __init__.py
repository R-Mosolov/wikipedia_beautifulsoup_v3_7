from modules import sciences_pages
from modules import scientists_pages
from modules import life_dates

print('\n===== ЭТАП №1. СБОР СТРАНИЦ НАУЧНЫХ НАПРАВЛЕНИЙ =====\n')
sciences_pages.run()

print('===== ЭТАП №2. СБОР СТРАНИЦ УЧЕНЫХ =====\n')
scientists_pages.run()

print('===== ЭТАП №3. СБОР И ОБРАБОТКА ВОЗРАСТОВ УЧЕНЫХ =====\n')
life_dates.run()
