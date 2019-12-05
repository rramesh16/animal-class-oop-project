from animal_class import *

class Dogs ():
    def __init__(self, name, owner, dog_collar):
        self.alive = True
        self.bones = True
        self.name = name
        self.owner = owner
        self.dog_collar = dog_collar



    def eat_bone(self):
        return 'Mmmm...Crunchy!'

    def run(self):
        return "can't catch up with me"

    def greet_owner(self):
        return "Give me attention Huoooman!"

    def make_sound(self):
        return 'Woof'
