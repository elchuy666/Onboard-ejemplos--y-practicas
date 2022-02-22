from datetime import timedelta, datetime

def distance_from_earth(destination):
    if destination == 'Moon':
        return '238,855'
    else:
        return 'Unable to compute to that destination'
distance_from_earth('moon')

distance_from_earth('Saturn')

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24
days_to_complete(238855, 75)

total_days = days_to_complete(238855, 75)
round(total_days)

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f'{destination} Arrival: %A %H:%M')
arrival_time('Moon')

def variable_length(*args):
    print(args)
variable_length()
variable_length('one', 'two')
variable_length(None)

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f'Total time to launch is {total_minutes} minutes'
    else:
        return f'Total time to launch is {total_minutes/60} hours'
    
sequence_time(4, 14, 48)

def variable_length(**kwargs):
    print(kwargs)
variable_length(tanks=1, day='Wednesday', pilots=3)

def crew_members(**kwargs):
    print(f'{len(kwargs)} astronauts assigned for this mission:')
    for title, name in kwargs.items():
        print(f'{title}: {name}')
crew_members(captain='Neil Armstrong', pilot='Buzz Aldrin', command_pilot='Michael Collins')