#Applied 7.2 (Please implement your character classes after the end of GeneralClass below)
import random
import math

class GeneralClass:

    """ General character class for representing and manipulating characters in the video game. """
    
    # Class Variable.
    character_tuple = ('Knight', 'Archer', 'Mage', 'Super Mage')
    move_list = ['regular_attack']

    def __init__(self): # Constructor.
        """ Create a general character. """
        self.name = None
        self.health = None
        self.power = None
        self.move_list = self.move_list[:]
        self.death_cry = None

    # Methods
    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_power(self):
        return self.power

    def get_move_list(self):
        return self.move_list

    def get_death_cry(self):
        return self.death_cry

    def get_character_tuple(self):
        return self.character_tuple

    def set_name(self, name):
        self.name = name

    def set_health(self, health):
        self.health = health

    def set_power(self, power):
        self.power = power

    def set_death_cry(self, death_cry):
        self.death_cry = death_cry

    def hit(self, scale, random_lb, random_ub):
        return math.ceil(random.uniform(random_lb, random_ub) * self.get_power() * scale)

    def get_hit(self, damage):
        self.set_health(max(self.get_health()-damage, 0))
        if self.get_health() == 0:
            print(self.get_death_cry())

    def rand_move(self):
        return self.get_move_list()[random.randrange(0, len(self.get_move_list()))]

# Please implement your character classes below.

class KnightClass(GeneralClass):

    move_list = ['regular_attack', 'spear_attack']

    def __init__(self):

        self.name = "Knight"
        self.health = random.randint(10, 15)
        self.power = random.randint(2, 4)
        self.move_list = self.move_list
        self.death_cry = 'Arrrrgh!'

    def hit(self, move):
        if move == 'regular_attack':
            return GeneralClass.hit(self, 1, 0.9, 1.1)
        if move == 'spear_attack':
            return GeneralClass.hit(self, 1.1, 0.7, 1.4)

class ArcherClass(GeneralClass):

    move_list = ['regular_attack', 'bow_attack']

    def __init__(self):
        self.name = 'Archer'
        self.health = random.randint(7, 13)
        self.power = random.randint(3,5)
        self.move_list = self.move_list[:]
        self.death_cry = 'Eeeeek!'

    def hit(self, move):
        if move == 'regular_attack':
            return GeneralClass.hit(self, 1.2, 0.9, 1.1)
        if move == 'bow_attack':
            return GeneralClass.hit(self, 1.5, 0.7, 1.3)


class MageClass(GeneralClass):

    move_list = ['regular_attack', 'spell_attack']

    def __init__(self):

        self.name = 'Mage'
        self.health = random.randint(19, 23)
        self.power = random.randint(1, 3) 
        self.move_list = self.move_list[:]
        self.death_cry = ('Noooo!')

    def hit(self, move):
        if move == 'regular_attack':
            return GeneralClass.hit(self, 1, 0.6, 1)
        if move == 'spell_attack':
            return GeneralClass.hit(self, 0.9, 0.8, 0.9)


class SuperMageClass(GeneralClass):

    move_list = ['regular_attack', 'spell_attack', 'super_spell_attack']

    def __init__(self):

        self.name = 'Super Mage'
        self.health = random.randint(22, 25)
        self.power = random.randint(3, 5) 
        self.move_list = self.move_list[:]
        self.death_cry = ('-.-')

    def hit(self, move):
        
        if move == 'regular_attack':
            return GeneralClass.hit(self, 1, 0.6, 1)

        if move == 'spell_attack':
            return GeneralClass.hit(self, 0.9, 0.8, 0.9)

        if move == 'super_spell_attack':
            return GeneralClass.hit(self, 1, 1.2, 1.7)