'''
TO RUN THIS FILE:
1) Start the Django Shell:
    
--> python manage.py shell

2) Load and run a file:

EXAMPLE 1
>>> exec(open('data_layer.py').read())

EXAMPLE 2
>>> exec(open('apps/generated_world/data_layer.py').read())

'''

# for club in m.Club.objects.all():
#     print('{} --> \t{}'.format(club.league.name, club.name))

# for league in m.League.objects.filter(sport__contains='ball'):
#     print('{} - {}'.format(league.sport, league.name))
#     for club in league.clubs.all():
#         print('\t{}'.format(club.name))

# for city in m.City.objects.filter(population__lt=15000).order_by('-population'):
#     print('{}\t{}'.format(city.population, city.name))

# for club in m.Club.objects.filter(memberships__person__last='Smith'):
#     print(club.name)
#     for membership in club.memberships.filter(person__last='Smith'):
#         print('\t{} {}'.format(membership.person.first, membership.person.last))