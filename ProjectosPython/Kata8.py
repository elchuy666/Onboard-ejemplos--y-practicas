planet = {
    'name': 'Mars',
    'moons': 2
}
print(f"{planet.get('name')} has {planet.get('moons')} moons")
planet['circunferencia (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}
print(f"{planet['name']} has polar circunference of {planet['circunferencia (km)']['polar']}")

planets_moons={
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'makemake': 1,
    'eris': 1
}
moons=planets_moons.values()
planets = len(planets_moons.keys())
total_moons=0
for moon in moons:
    total_moons = total_moons + moon
average = total_moons / planets
print(average)