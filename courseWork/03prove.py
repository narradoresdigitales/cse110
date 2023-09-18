'''
filename: 02prove.py
author: msilp 
purpose: In this assignment, you will write a program to calculate the price of a meal

'''

# At the end of Lesson 03, to help make sure you are on track to finish the assignment, you need to complete the following:

# Ask the user for the price of a child and an adult meal and store these values properly into variables as floating point numbers.

# Ask the user for the number of adults and children and store these values properly into variables as integers.

# Ask the user for the sales tax rate and store the value properly as a floating point number.

# Compute and display the subtotal (don't worry about rounding to two decimals at this point).


'''
Ask the user for the following:

The price of a child's meal (floating point)

The price of an adult's meal (floating point)

The number of children (integer)

The number of adults (integer)

The sales tax rate (floating point)


'''


child_meal = float(input('What is the price of a meal for a child?'))
adult_meal = float(input('What is the price of a meal for an adult?'))
num_children = int(input('How many children are there?'))
num_adults = int(input('How many adults are there?'))
sales_tax = float(input('What is the sales tax?'))
meal_cost_child = child_meal * num_children
meal_cost_adult = adult_meal * num_adults
subtotal = meal_cost_child + meal_cost_adult
sales_tax_to_add = subtotal * sales_tax / 100
total_with_tax = subtotal + sales_tax_to_add
currency_subtotal = "${:,.2f}".format(subtotal)
currency_sales_tax = "${:,.2f}".format(sales_tax_to_add)
currency_total = "${:,.2f}".format(total_with_tax)
print('Subtotal:' + str(currency_subtotal))
print('Sales Tax:' + str(currency_sales_tax))
print('Total:' + str(currency_total))
print()
payment = float(input('What is the payment amount?'))
change = payment - total_with_tax
currency_change = "${:,.2f}".format(change)
print('Change:' + str(currency_change))


# _check__Include a dollar sign ($) before each displayed value.
'''
currency_string = "${:,.2f}".format(number_string)
print(currency_string) 
'''
# working___Double check that the calculations are correct.
# working___Show creativity and exceed the core requirements by adding additional features.
# working___Use good style in your program, including variable names and whitespace.

# (I'll keep working on these items this week).

'''
Milestone Requirements
At the end of Lesson 03, to help make sure you are on track to finish the assignment, you need to complete the following:

__check___Ask the user for the price of a child and an adult meal and store these values properly into variables as floating point numbers.

__check___Ask the user for the number of adults and children and store these values properly into variables as integers.

_check____Ask the user for the sales tax rate and store the value properly as a floating point number.

__check___Compute and display the subtotal (don't worry about rounding to two decimals at this point).

'''

'''
Final requirements
At the end of Lesson 04, in addition to the milestone requirements above, you need to also complete the following:

_check___Compute and display the sales tax.

_check___Compute and display the total.

_check___Ask the user for the payment amount and store the value properly as a floating point number.

_check___Compute and display the change.

_check___Display each value to two decimals.




'''
