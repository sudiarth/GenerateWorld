import django
from django.db.models import Count, Sum
import apps.generated_world.models as m


django.setup()

#Level 1
# +++++++++++++++++++++++++++++++

# 1. Returns all the state capitals 
def get_all_the_state_capitals():
    for capital in m.City.objects.filter(is_capital=1):
        print('{} --> \t{}'.format(capital.state.name, capital.name))

# get_all_the_state_capitals()

# 2. Returns all cities in reverse order by population
def get_all_cities_in_reverse_order_by_population():
    for city in m.City.objects.all().order_by('-population'):
        print('{}\t{}'.format(city.population, city.name))

#get_all_cities_in_reverse_order_by_population()

#3. Takes in a string (sport) and returns the leagues for that sport
def get_the_leagues_by_name(sport):
    for league in m.League.objects.filter(sport=sport):
        print('{} - {}'.format(league.sport, league.name))
        for club in league.clubs.all():
            print('\t{}'.format(club.name))

# get_the_leagues_by_name('Hockey')

# 4. Takes in a string (name_fragment) and returns the clubs that contain that string in their name
def get_clubs_by_name(club_name):
    for club in m.Club.objects.filter(name__contains=club_name):
        print('{}'.format(club.name))

# get_clubs_by_name('south')

# 5. Takes in a string (name_fragment) and returns the companies that do not contain that string in their name
def get_companies_by_name(company_name):
    for company in m.Company.objects.filter(name__contains=company_name):
        print('{}'.format(company.name))

# get_companies_by_name('ock')

# 6. Takes in a float and returns the companies that have a net income below that float
def get_companies_income_less_than(income):
    for company in m.Company.objects.filter(net_income__lt=income).order_by('-net_income'):
        print('{}\t{}'.format(company.name, company.net_income))

# get_companies_income_less_than(2000)

# 7. Takes in an integer and returns the streets that match that integer
def get_street_by_number(number):
    for address in m.Address.objects.filter(street__startswith=number):
        print('{}'.format(address.street))

# get_street_by_number(1339)

# 8. Takes in two integers and finds the cities with a population between those two integers
def get_cities_by_population(less, bigger):
    for city in m.City.objects.filter(population__lte=bigger, population__gt=less):
        print('{} - {}'.format(city.name, city.population))

# get_cities_by_population(10000, 20000)

# 9. Takes in a cardinal direction and returns the cities that contain that are named accordingly
def get_cities_by_direction_by(cardinal):
    for city in m.City.objects.filter(name__startswith=cardinal):
        print('{}'.format(city.name))
    
# get_cities_by_direction_by('west')

# 10. Takes in a company association and returns the companies that contain that company association
def get_companies_association_by(type):
    for company in m.Company.objects.filter(name__contains=type):
        print('{}'.format(company.name))

# get_companies_association_by('ltd')


#Level 2
# +++++++++++++++++++++++++++++++

# 1. Takes in a string (department) and returns the companies that have that department
def get_companies_by(department):
    for company in m.Company.objects.filter(departments__name=department):
        print('{}'.format(company.name))

# get_companies_by('Engineering')

# 2. Finds all the people who are currently employed
def get_people_by_current_employee():
    for employee in m.Employment.objects.filter(is_employed=1):
        print('{}'.format(employee.person.first + employee.person.last))

# get_people_by_current_employee()

# 3. Finds all the people who currently play for a given club
def get_people_currently_play_club(club_name):

    for person in m.Person.objects.filter(memberships__is_active=1, memberships__club__name=club_name):
        print(person.id, person.first, person.last)

    club = m.Club.objects.get(name=club_name)
    print(club.id)
    # for membership in club.memberships.filter(is_active=1):
    #     print(membership.person.first)
    
    # for person in m.Person.objects.filter(memberships__club__name=club_name):
    #     for membership in person.memberships.filter(is_active=1):
    #         print('{} {} {} {}'.format(membership.club.name, membership.is_active, membership.person.first, membership.person.last))

# get_people_currently_play_club('Alfano City Broncos')

# 4. Finds all past addresses for a given person
def get_addresses_by_person(person_id):
    for address in m.Address.objects.filter(is_current=0, person__id=person_id):
        print(address.street)

# get_addresses_by_person(2)

# 5. Finds all the companies for a given industry
def get_companies_by_industry(industry_name):
    for company in m.Company.objects.filter(listings__industry=industry_name):
        print(company.name)

# get_companies_by_industry('Transportation')

# 6. Finds all the clubs for a given league
def get_clubs_by_league(league_name):
    for club in m.Club.objects.filter(league__name=league_name):
        print(club.name)

# get_clubs_by_league('Global Baseball League')

# 7. Finds the state with the most number of cities
def get_state_by_most_city():
    for state in m.State.objects.annotate(count=Count('cities')).order_by('-count'):
        print('{} - {}'.format(state.name, state.count))

# get_state_by_most_city()

# 8. Finds the most populous state
def get_state_by_most_populous():
    for state in m.State.objects.annotate(count=Sum('cities__population')).order_by('-count'):
        print('{} - {}'.format(state.name, state.count))

# get_state_by_most_populous()

# 9. Finds the total assets for a given industry
def get_total_assets_by_industry(industry_name):
    for company in m.Company.objects.filter(listings__industry=industry_name).annotate(total=Sum('total_assets')).order_by('-total'):
        print('{} - {}'.format(company.name, company.total))

# get_total_assets_by_industry('Transportation')

# 10. Find the companies for a given industry after a certain date
def get_companies_by_industry_and_by_founded(industry_name, date):
    for company in m.Company.objects.filter(listings__industry=industry_name, founded_on__gte=date):
        print('{}'.format(company.name))

# get_companies_by_industry_and_by_founded('Transportation','1990-05-11')

# Level 3
# +++++++++++++++++++++++++++++++

# 1. Returns the states in descending order by the number of cities they have
def get_states_by_cities():
    for state in m.State.objects.annotate(count=Count('cities')).order_by('-count'):
        print('{} - {}'.format(state.name, state.count))

# get_states_by_cities()

# 2. Returns the clubs that have the most past memberships
def get_most_club_by_past_membership():
    for club in m.Club.objects.annotate(count=Count('memberships')).filter(memberships__is_active=0).order_by('-count'):
        print('{} - {}'.format(club.name, club.count))

# get_most_club_by_past_membership()

# 3. Returns the exchanges in descending order by the number of listings they have
def get_exchanges_by_listings():
    for exchange in m.Exchange.objects.annotate(count=Count('listings__exchange')).order_by('-count'):
        print('{} - {}'.format(exchange.name, exchange.count))

# get_exchanges_by_listings()

# 4. Returns the companies with the most number of departments
def get_companies_by_departments():
    for company in m.Company.objects.annotate(count=Count('departments')).order_by('-count'):
        print('{} - {}'.format(company.name, company.count))

# get_companies_by_departments()

# 5. Returns the cities with the most employed people
def get_cities_by_most_employee():
    for city in m.City.objects.annotate(count=Count('addresses__person__jobs')).order_by('-count'):
        print('{} - {}'.format(city.name, city.count))

# get_cities_by_most_employee()

# 6. Returns the most profitable industries
def get_most_profitable_industries():
    for industry in m.Listing.objects.annotate(count=Count('company__revenue')).order_by('-count'):
        print('{} - {}'.format(industry.company.name, industry.count))

get_most_profitable_industries()