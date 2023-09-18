''' 
filename: 02teach.py
author: msilp 
purpose: print to screen

'''

first_name = input('Type your First name.')
last_name = input('Type your Last name.')
email = input('Type your Email.')
phone = input('Type your Phone Number.')
job_title = input('Type your Job Title.')
id_num = input('Type your ID Number.')
hair = input('What color is your hair?')
eyes = input('What color are your eyes?')
month = input('Enter the month you started employment.')
training = input('Have you completed advanced training?')

print(last_name.upper() + ',' + '' + first_name)
print(job_title.capitalize())
print('ID:' + ' ' + id_num)
print()
print(email)
print(phone)
print()
print('Hair:' + ' ' + hair.capitalize() +
      '     ' + 'Eyes:' + ' ' + eyes.capitalize())
print('Month:' + ' ' + month.capitalize() + '     ' +
      'Training:' + ' ' + training.capitalize())
