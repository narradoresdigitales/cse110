''' 
filename: 02prove.py
author: msilp 
purpose: create a word game/have fun
'''
# I looked up how to print in colors
from termcolor import colored
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


adjective = input('Type an adjective:')
adjective = 'RED'
animal = input('Type the name of an animal:')
verb = input('Type a verb:')
exclamation = input('Type an exclamation!:')
verb2 = input('Type a second verb:')
verb3 = input('Type a third verb:')
print('Your story is:')
print()

prGreen('The other day, I was really in trouble. It all started when I saw a very \n' + ' ' +
        # + exclamation.upper()  + '!') I had to research how to use f-strings to place variable in quotation marks(still no exactly sure why it works :)
        # then I adjusted the string concatenation to achieve the desired format.
        (adjective + ' ' + animal) + ' ' + \
        'sneeze down the hallway.' + ' '
        + f'"{exclamation.upper()}"' + '!' + ' '
        # print(colored(exclamation.upper(),'red')) -- I could not get this to work. I'll continue to troubleshoot.
        + 'I yelled. But all \n I could think to do was to' +
        ' ' + verb2 + ' ' + 'over and over. Miraculously, \n that caused it to stop, but not before it tried to' + ' ' +
        verb3 + ' ' + '\n right in front of my family.')
