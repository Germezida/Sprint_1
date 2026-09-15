world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина'

country = 'Италия'

for year, champion in world_champions.items(): 
    print(f'{year} - {champion}')

if country in world_champions.values():
   print(f'Италия cтановилась чемпионом мира по футболу в 21 веке!')
else:
    print(f'Италия не выигрывала чемпионат мира по футболу в 21 веке.')