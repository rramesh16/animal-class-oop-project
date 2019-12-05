from animal_class import *
from dog_class import *

dog1 = Dogs('Nala', 'Griffen', 'N the best')
dog2 = Dogs('Teddy', 'Sarah', "If I am lost, call Sarah")

print(dog1.name)
print(dog1.owner)
print(dog1.dog_collar)
print(dog1.make_sound())

print(dog2.name)
print(dog2.owner)
print(dog2.dog_collar)
print(dog2.greet_owner())