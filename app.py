import math

print("Tharunie De Silva")
print('o----')
print(' ||||')
print('*' * 10)
price = 10
price = 20
rate = 2.3456
name = 'Tharunie'
value = True
print(value)
print(name)
print(rate)
print(price)

fullname = 'John'
age = 56
isNew = True
print(f'{fullname} {age} {isNew}')
# name = input('What is your name ')
# print(f'HI {name}')
# favColor = input('What is your favourite color ')
# print(f'Favourite color of {name} is {favColor}')

birth_year = input('Birth Year: ')
age_ForNow = 2020 - int(birth_year)
print(type(age_ForNow))
print(type(birth_year))
print(age_ForNow)
weight_In_Pounds = input('Enter your weight in pounds: ')
print(f'Weight in kgs : {float(weight_In_Pounds)*0.45}')
course = 'Pyhon for beginners'
print(course[0])
print(course[-1])
print(course[0:-3])
name = 'Jennifer'
print(name[1:-1])
first = 'Jhon'
last = 'Smith'
print(f'{first} {last}')
courseName = 'Python for beginners'
print(len((courseName)))
print(courseName.upper())
print(courseName.lower())
print(courseName.find('P'))
print(courseName.find('O'))
print(courseName.replace('beginners', 'Absolute Beginners'))
print('Python' in courseName)
x = 2.9
print(abs(x))
print(round(x))
final = 2**4*5/8+7-8
print(final)
print(math.ceil(rate))
print(math.floor(x))

temp_in_Farenhite=input("Enter today's temperature in Faranhite ")
temp_in_Centigrade = (float(temp_in_Farenhite) -32)*(5/9)
print(round(temp_in_Centigrade))
if round(temp_in_Centigrade)>30:
    is_hot = True
    is_cold=False
elif round(temp_in_Centigrade)<= 20:
    is_hot = False
    is_cold = True
else:
    is_hot = False
    is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes')
else:
    print("It's a lovely day")
print("Enjoy your day")

house_amount = input("Enter the price of the house ")
buyer_credit = input("Enter your Account Number ")

hasGoodCredit = False
if buyer_credit == '1111122222':
    hasGoodCredit = True
elif buyer_credit == '1000000000':
    hasGoodCredit = False
else:
    hasGoodCredit =False

if hasGoodCredit:
    balance = float(house_amount)-float(house_amount)*0.1
    print("You have a good credit")
else:
    balance = float(house_amount)-float(house_amount)*0.2

print(f'Your down payment is ${math.trunc(balance)}')



has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Loan can be granted")
else:
    print("Loan cannot be granted")
user_name=input("Enter your name ")
if len(user_name)<=3:
    print("Invalid Name")
elif len(user_name)<=10 and len(user_name)>3:
    print("Valid Name")
else:
    print("Name is too long. Enter another one")

weight_of_user = input("Weight ")
get_Letter = input("(L)bs or (K)g : ")

if get_Letter.upper()=='L':
    print(f'You are {math.ceil(float(weight_of_user)*(0.45))} kgs')
elif get_Letter.upper()=='K':
    print(f'You are {math.ceil(float(weight_of_user) / 0.45)} pounds')
else:
    print('Wrong Input')