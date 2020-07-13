'''
orbital radius mln km
orbital speed mln km per day
86400 sec = 1 day
'''
import math

planets = {'Mercury': {'orbital_radius': 58,   'orbital_speed': 4.135968},
             'Venus': {'orbital_radius': 108,  'orbital_speed': 3.025728},
             'Earth': {'orbital_radius': 150,  'orbital_speed': 2.571264},
              'Mars': {'orbital_radius': 228,  'orbital_speed': 2.084832},
            'Upiter': {'orbital_radius': 778,  'orbital_speed': 1.129248},
            'Saturn': {'orbital_radius': 1429, 'orbital_speed': 0.835488},
              'Uran': {'orbital_radius': 2871, 'orbital_speed': 0.590976},
            'Neptun': {'orbital_radius': 4504, 'orbital_speed': 0.473472},
           }

def orbit_len(orbit_rad):
    return 2 * math.pi * orbit_rad

def days_in_year(orbit_rad, orbit_speed):
    try:
        return orbit_len(orbit_rad) / orbit_speed
    except ZeroDivisionError:
        print(f'Planet has 0 in speed value')

try:
    planet = input("Enter planet:").lower().capitalize()

    for t in planets:
        planets[t].update({'days in year': days_in_year(planets[t]['orbital_radius'], planets[t]['orbital_speed'])})

    print(f"Planet {planet}: orbital radius = {planets[planet]['orbital_radius']}; orbital speed = {planets[planet]['orbital_speed']};", end='')
    print(f" days in year = {days_in_year(planets[planet]['orbital_radius'], planets[planet]['orbital_speed'])};")
    max_year = max([opt['days in year'] for name, opt in planets.items()])

    for t in planets:
        if planets[t]['days in year'] == max_year:
            print(f'The longest year has planet {t} = {max_year} days')
            break

    planets_years = {days_in_year(days['orbital_radius'], days['orbital_speed']): name for name, days in planets.items()}
    print(f"The longest year has planet {planets_years[max(planets_years.keys())]} = {max(planets_years.keys())} days ")

except KeyError:
    print(f'Wrong name of planet {planet}')
