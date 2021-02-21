import  converters
from ecommerce.shipping import calc_shipping
from converters import kgs_to_lbs
from utils import find_max
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self):
        print('Move')

    def draw(self):
        print('draw')

point1 = Point(10,20)
print(point1.x)
print(point1.y)
point1.draw()


class Person():
    def __init__(self,name):
        self.name = name


    def talk(self):
        print(f'Hello {self.name} !! Nice to Meet you')


andrew = input('>Enter your Name: ')
person = Person(andrew)
person.talk()
print()
bob = input('>Enter Name: ')
person2 = Person(bob)
person2.talk()
print()

class Mammal:
    def walk(self):
        print('Walk')

class Dog(Mammal):
    def bark(self):
        print('Bark')


class Cat(Mammal):
    def mew(self):
        print('Mew')


d1 = Dog()
d1.walk()
d1.bark()

c1 = Cat()
c1.walk()
c1.mew()

print(converters.lbs_to_kg(145))
print(kgs_to_lbs(49))
print(find_max([1, 34, 56, 2, 3, 67, 299, 1, 23]))
calc_shipping()
