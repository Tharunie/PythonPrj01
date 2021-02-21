numbers = (1,2,3)
coordinates= (1,2,3)
x,y,z = coordinates
print(x)
print(y)
print(z)

customer ={
    "name":'John Smith',
    "age":30,
    "is_verified": True
}
customer['name'] = 'Jack Smith'
customer["birthDate"]='Aug 10 1995'
print(customer["name"])
print(customer.get('age'))
print(customer.get('birthDate'))

phone = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}
phone['0'] = 'Zero'
phone_number = input('Phone: ')
for num in phone_number:
    print(phone.get(f'{num}'), end=' ')
print()
message = input('> ')
words = message.split(' ')
emojis = {
    ":)":" 😀",
    ":(":"😞",
    ":-|":"😏",
    ":D":"😂"
}
for word in words:
    print(emojis.get(word,"word"),end=' ')






