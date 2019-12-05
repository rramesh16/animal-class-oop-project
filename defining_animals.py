from animal_class import *
from dog_class import *

animal1 = Animals('Simba', 'Mammal')
animal2 = Animals('Henry', 'Reptile')

print(animal1.name)
print(animal1.type)
print(animal1.make_sound())

print(animal2.name)
print(animal2.type)
print(animal2.eat('chicken'))
