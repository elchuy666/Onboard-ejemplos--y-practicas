'''user_input=''

inputs =[]

while user_input.lower() !='done':
    if user_input:
        inputs.append(user_input)
        
    user_input = input('Enter a new value, or done when done ')'''

'''countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
print("Blast off!! 🚀")'''

# De la biblioteca time, importamos (traemos) la clase sleep

from time import sleep

# Creamos una lista de 5 números llamada countdown
countdown = [4, 3, 2, 1, 0]

# Para cada número en countdown
for number in countdown:
    #Muestra el número
    print(number)

    # Espera (1segundo)
    sleep(1)

# Muestra el mensaje Blast off
print("Blast off!! 🚀")
