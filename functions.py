def greet_user():
    print('Hi There...')
    print('Welcome Abord...')


print('Start')
greet_user()
print('Finish')

def student_details(name,age,dept):
    print('Hi '+name)
    print('You are '+age+' years old')
    print('Your dept is '+dept)


print('Start')
std_name = input('Enter Name: ')
std_age = input('Enter age: ')
std_dpt = input('Enter Department: ')
student_details(std_name, std_age, std_dpt)
print('End')

student_details(age='45',dept='IT',name='Tharanija')
student_details('Amaya',dept='FD',age='23')
print('End')

def square(number):
    return number*number


print(square(3))

def generate_emojis(emoji):
    words = message.split(' ')
    emojis = {
        ":)": " 😀",
        ":(": "😞",
        ":-|": "😏",
        ":D": "😂"
    }
    for word in words:
        print(emojis.get(word, word), end=' ')


message = input('> ')
generate_emojis(emoji=message)
print()

try:
    age = int(input('Age: '))
    income = 200000
    risk = income/age
    print(risk)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalid Error')







