i = 1
while i <= 5:
    print(i)
    i += 1
print("Done")

j = 1
while j <= 5:
    print('*' * j)
    j += 1
print("Done")

print("Welcome to Guess Game")
guess_number = 9
guess_count = 1
while guess_count <= 3:
    var = input('Guess: ')
    guess_count += 1
    if int(var) == guess_number:
        guess_count += 1
        print('You won')
        break
else:
    print('All your Guess Chances are over')

is_started = False
count_of_stop = 0
while True:
    user_input = input('> ').lower()
    if user_input == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif user_input == 'start':
        is_started =True
        if is_started:
            print('The car has already started')
        else:
            print('Car started...Ready to go!')

    elif user_input == 'stop':
        if not is_started:
            print('Hey! The car is already stopped...')
        else:
            is_started = False
            print("Car stopped...")
    elif user_input != 'quit':
        print('I dont understand that...')
    else:
        break


prices = [10, 20, 30]
sum = 0
for number in prices:
    sum += number
print(sum)

for x in range(4):
    for y in range(4):
        print(f'({x}, {y})')

numbers = [1, 1, 1, 1, 5]
for number in numbers:
    for num in range(number):
        print('X', end='')
    print()

names = ['Jhon', 'Sara', 'Dave', 'Mosh', 'Derick', 'Peter']
print(names)
print(names[2])
print(names[-1])
print(names[2:5])
print(names[2:])

number_List = [1, 56, 78, 2, 90, 4, 3, 12, 3, 5]
max_number = number_List[0]
for number in number_List:
    if max_number < number:
        max_number = number
print(f'The maximum number in the List is {max_number}')

matrix =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for x in range(3):
    for y in range(3):
        print(matrix[x][y], end=' ')
    print()

prices = [122,342,321,122,234]
prices.append(123)
prices.insert(0,1000)
prices.remove(1000)
prices.pop()
print(prices.count(122))
print(prices.index(321))
prices.sort()
prices.reverse()
print(122 in prices)
for price in prices:
    print(price)

print(prices)

item_prices = [234, 1234, 67, 89, 54, 1234, 56, 89, 67, 1235, 5600, 34, 54, 67]
item_prices.sort()

i = 0
uniques = []
for item in item_prices:
    if item not in uniques:
        uniques.append(item)
print(uniques)


