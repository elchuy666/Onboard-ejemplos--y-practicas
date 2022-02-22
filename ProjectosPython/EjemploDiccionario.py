planet = {
    'name': 'Earth',
    'moons': 1
}
print(planet['name'])

#planet.update({'name': 'Makemake'})
planet['name'] = 'Makemake'

planet['name'] = 'Jupiter'
planet['moon'] = 79
planet['Orbital period'] = 4333
planet.pop('Orbital period')

planet['diameter (km)'] ={
    'polar': 133709,
    'equatorial': 142984
}

print(f"{planet['name']} polar diameter: {planet['diameter (km)']['polar']}")
