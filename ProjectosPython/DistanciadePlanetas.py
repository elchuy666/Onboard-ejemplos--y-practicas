planetas = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print('There are', len(planetas), 'planets')
planetas.append('Pluton')
print(planetas[-1], 'is the last planet')

user_planet=input('Please enter the name of the planet (with a capital letter to start)')
planetas_index=planetas.index(user_planet)

print('Here are the planets closer to the sun than ' + user_planet)
print(planetas[0:planetas_index])

print('Here are the planets further to the sun than ' + user_planet)
print(planetas[planetas_index + 1:])

planetas.pop()  # Goodbye, Pluto
number_of_planets = len(planetas)
print('No, there are definitely', number_of_planets, 'planets in the solar system.')
