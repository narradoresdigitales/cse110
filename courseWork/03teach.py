'''

filename: 03prove.py
author: msilp
purpose: Create a program that calculates the area of shapes. Use variables and expressions in python.

'''
#caculate area of user square
length_of_square = input('What is the length of your square?')
width_of_square = input('What is the width of your square?')
user_square_length =length_of_square
user_square_width =width_of_square
square_area = int(user_square_length) * int(user_square_width)
print(f'The area of your is square is {square_area}.') 

#caculate area of user circle
circle_radius = input('What is the radius of your circle?')
circle_area = int(circle_radius)*int(circle_radius)*3.14
print(circle_area)

#caculate area of user triangle
triangle_base = input('What is the base of your triangle?')
triangle_height = input('What is the height of your triangle?')
triangle_area = int(triangle_base)*int(triangle_height)/2
print(f'The area of your triangle is {triangle_area}.')

