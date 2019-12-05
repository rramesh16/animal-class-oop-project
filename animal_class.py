
class Animals ():
    def __init__(self, name, type):
        self.alive = True
        self.bones = True
        self.name = name
        self.type = type



    def eat(self, food):
        return 'NOM NOM NOM!' + food

    def sleep(self):
        return 'Zzzzz'

    def make_sound(self):
        return 'animal sound'


