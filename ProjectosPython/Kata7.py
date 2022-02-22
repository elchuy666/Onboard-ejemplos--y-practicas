new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet ')


for planet in planets:
    print(planet)
