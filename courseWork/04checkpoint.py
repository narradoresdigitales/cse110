'''
file: 04checkpoint.py
author:msilp
purpose: Convert degrees in Fahrenheit to Celsius and from Celsius to Fahrenheit

'''
# Fahrenheit to Celsius converter  
user_degree_fahrenheit = input('Enter degrees in Fahrenheit:')
print(f'Lets convert {user_degree_fahrenheit} to degrees in Celsuis.')
print(f'Calculating ...')
degrees_in_Celsius = int(user_degree_fahrenheit) - 32 / 9
print(f'{user_degree_fahrenheit} is {degrees_in_Celsius} degrees Celsius!')


# Celsius to Fahrenheit converter
print('This program will convert Celsius to Fahrentheit.')
user_degree_Celsius = input('Enter degrees in Celsius:')
print(f'Lets convert {user_degree_Celsius} to degrees in Fahrenheit.')
user_guess = input('Can you guess the answer? What do you think is the answer? ')
print(f'Calculating ...')
degrees_in_Fahrenheit = int(user_degree_Celsius) * 2 + 30
print(f'You guessed {user_guess} degrees Fahrenheit.')
print(f'The answer is: {degrees_in_Fahrenheit} degrees Fahrenheit!')