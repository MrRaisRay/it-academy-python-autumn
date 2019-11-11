import random


class Random_Enemy(object):
    def __init__(self):
        self.hp = random.randrange(60, 100, 1)

    def atack(self):
        return random.randrange(15, 30, 1)


class Treasure(object):
    def __init__(self):
        global hero
        self.name = random.choice(['Icarus wings', 'Gephestus hammer', 'Zeus lightning'])
        if self.name == 'Gephestus hammer':
            self.effect = 'Strenght +1'
            hero.strength += 1
            hero.finding_treasures.append(self.name)
        elif self.name == 'Icarus wings':
            self.effect = 'Agility +1'
            hero.agility += 1
        elif self.name == 'Zeus lightning':
            self.effect = 'Intellect +1'
            hero.intellect += 1


class Hero(object):
    char_class = ''

    def __init__(self, char_c='Warrior'):
        self.char_class = char_c
        if self.char_class == 'Warrior':
            self.strength = 10
            self.agility = 7
            self.intellect = 3
        elif self.char_class == 'Rogue':
            self.strength = 5
            self.agility = 10
            self.intellect = 5
        elif self.char_class == 'Mage':
            self.strength = 4
            self.agility = 2
            self.intellect = 14
        self.hp = self.strength * 15
        self.mp = self.intellect * 15
        self.dodge = self.agility * 2
        self.finding_treasures = []

    def atack(self):
        if self.char_class == 'Warrior':
            return self.strength * random.randrange(1, 3, 1)
        elif self.char_class == 'Rogue':
            return self.strength * random.randrange(1, 3, 1)
        elif self.char_class == 'Mage':
            return self.strength * random.randrange(1, 3, 1)

    def ability(self):
        if self.char_class == 'Warrior':
            if self.mp >= 8:
                print("Hero using Axe Smash")
                dmg = self.strength * random.randrange(3, 7, 1)
                self.mp -= 8
            else:
                print("Mana low")
                dmg = 0
        elif self.char_class == 'Rogue':
            if self.mp >= 15:
                print("Hero using Backstep")
                dmg = self.agility * random.randrange(3, 7, 1)
                self.mp -= 15
            else:
                print("Mana low")
                dmg = 0
        elif self.char_class == 'Mage':
            if self.mp >= 30:
                print("Hero using Exterminatus")
                dmg = self.intellect * random.randrange(3, 7, 1)
                self.mp -= 30
            else:
                print("Mana low")
                dmg = 0
        return dmg

    def __str__(self):
        return (str(self.char_class) + ' escaping from dungeon\n' +
                "He's finding" + str(self.finding_treasures) + '\n' +
                "His condition: HP=" + str(self.hp) + " MP=" + str(self.mp))


rooms_counter = 1


def print_state():
    print('HP=' + str(hero.hp) + " MP=" + str(hero.mp)+ " DG=" +
          str(hero.dodge))


def escape_from_dungeon():
    global hero
    print(hero)
    exit()


def next_room():
    global hero
    answer = str(input("Wanna you going to next room?(y/n)"))
    if answer == 'y':
        global rooms_counter
        rooms_counter += 1
        gm()
    elif answer == 'n':
        escape_from_dungeon()


def battle():
    new_enemy = Random_Enemy()
    while 1:
        attack_type = str(input("You wanna atack or use ability?(at/ab)"))
        if attack_type == 'at':
            new_enemy.hp -= hero.atack()
        elif attack_type == 'ab':
            new_enemy.hp -= hero.ability()
        if new_enemy.hp <= 0:
            print("Enemy died")
            print_state()
            break
        if hero.dodge < random.randrange(1, 100, 1):
            hero.hp -= new_enemy.atack()
            print_state()
        else:
            print("Hero dodge enemy attack")
        if hero.hp <= 0:
            print("You died")
            exit()


def treasure_hunt():
    new_treasure = Treasure()
    print("You find treasure.\n" +
          "It's " + str(new_treasure.name) + "\n" +
          "Effect: " + str(new_treasure.effect))
    hero.hp = hero.strength * 15
    hero.mp = hero.intellect * 15
    hero.dodge = hero.agility * 2
    print_state()


def met_enemy():
    print_state()
    print('You met the enemy')
    choice = input("Fight or run?(f/r)")
    if choice == 'f':
        battle()
    elif choice == 'r':
        hero.char_class = 'Pathetic coward'
        escape_from_dungeon()


def gm():
    global hero, rooms_counter
    print('You enter in room #' + str(rooms_counter))
    room_type = random.randrange(1, 4, 1)
    if room_type == 1:
        print('Room is empty')
        next_room()
    elif room_type == 2:
        met_enemy()
        next_room()
    elif room_type == 3:
        treasure_hunt()
        next_room()
    elif room_type == 4:
        met_enemy()
        treasure_hunt()
        next_room()


hero = Hero(str(input("Who are you stranger?(Warrior, Rogue or Mage)")))
print_state()
gm()
