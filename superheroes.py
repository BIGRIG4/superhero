import random

class Hero:

    def __init__(self, name, health = 100):
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0


    def defend(self):
        defence = 0
        if self.health > 0:
            for item in self.armors:
                defence += item.defend()
        return defence



    def take_damage(self, damage_amt):
        self.health -= damage_amt
        if self.health <= 0:
            self.deaths += 1
            return 1
        return 0



    def add_kill(self, num_kills):
        self.kills += num_kills



    def add_ability(self, ability):
        self.abilities.append(ability)


    def add_armor(self, armor):
         self.armors.append(armor)



    def attack(self):
        total_attack = 0
        if self.abilities != None:
            for ability in self.abilities:
                total_attack = total_attack + ability.attack()
        return total_attack

Ability Class

class Ability:

    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength



    def attack(self):
        lowest_attack = self.attack_strength // 2
        return  random.randint(lowest_attack, self.attack_strength)


    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength


 Weapon Class
class Weapon(Ability):
    def attack(self):
        return  random.randint(0, self.attack_strength)


ARMOR CLASS
class Armor:

    def __init__(self, name, defence):
        self.name = name
        self.defence = defence



    def defend(self):
        return random.randint(0, self.defence)


 TEAM CLASS
class Team:

    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()
        self.team_kills = 0


    def add_hero(self, Hero):
        self.heroes.append(Hero)



    def remove_hero(self, name):
        if self.name != None:
            for hero in self.view_all_heroes:
                if name in hero.name:
                    self.heroes.remove(hero)
                else:
                    return 0
        else:
            return 0



    def find_hero(self, name):
        if self.heroes != None:
            if name == hero.name:
                return hero
            else:
                return 0


    def view_all_heroes(self):
        for hero in self.heroes:
            name = hero.name
            print(name)



    def attack(self, other_team):
        attack_total = 0
        for hero in self.heroes:
            print(hero.name)
            attack_total += hero.attack()
        kills = other_team.defend(attack_total)
        self.team_kills += kills
        for hero in self.heroes:
            hero.add_kill(kills)



    def defend(self, damage_amt):
        defence = 0
        for hero in self.heroes:
            defence += hero.defend()
        if(damage_amt > defence):
            return self.deal_damage(damage_amt - defence)
        return 0



    def deal_damage(self, damage):
        deaths = 0
        for hero in self.heroes:
            deaths += hero.take_damage(damage / len(self.heroes))
        return deaths



    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            hero.health = hero.start_health



    def stats(self):
        for kill in self.heroes:
            print(kill.name + "Kills: " + str(kill.kills) + " Deaths:" + str(kill.deaths))






    def update_kills(self):
        for kill in self.heroes:
            kill.kills += 1


 ARENA CLASS
class Arena:

    def __init__(self, team_size):
        self.team_one = None
        self.team_two = None
        self.team_size = team_size



    def build_team_one(self):
        self.team_one = Team(input("What is the name of your team?: "))
        print("Hero time! Both teams have " + str(self.team_size) + " players")
        for i in range(self.team_size):
            print("Hero number {}. ".format(i))
            self.team_one.add_hero(create_hero())



    def build_team_two(self):
        self.team_two = Team(input("What is the name of the second team?: "))
        print("Hero Time! Both teams have " + str(self.team_size) + " players")
        for i in range(self.team_size):
            print("Hero number {}. ".format(i))
            self.team_two.add_hero(create_hero())



    def team_battle(self):
        while(self.team_one.team_kills < self.team_size and self.team_two.team_kills < self.team_size):
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)
            self.show_stats()



    def show_stats(self):
        self.team_one.stats()
        self.team_two.stats()




def create_hero():
    hero =  Hero(input("What is your heroes name: "))
    i = None
    while(i != "stop".lower()):
        hero.add_ability(create_ability())
        i = input("Do you want to add more? Press Enter to add more or type 'stop' to finish adding : ")

    i = None
    while( i != "stop".lower()):
        hero.add_ability(create_weapon())
        i = input("Do you want to add more? Press Enter to add more or type 'stop' to finish adding : ")

    i = None
    while(i != "stop".lower()):
        hero.add_armor(create_armor())
        i = input("Do you want to add more? Press Enter to add more or type 'stop' to finish adding : ")
    print("Your hero is now complete ")
    return hero



def create_ability():
    ability =  Ability(input("What is the abilities name?: "), int(input("What is its strength level?: ")))
    return ability


def create_weapon():
    weapon =  Weapon(input("What is the name of the weapon?: "), int(input("What is its strength level?: ")))
    return weapon


def create_armor():
    armor =  Armor(input("What is the name of the armor?: "), int(input("What is its strength level?: ")))
    return armor




if __name__=="__main__":
    battle_zone = Arena(int(input("How many heroes does your team have?: ")))
    running = True
    battle_zone.build_team_one()
    battle_zone.build_team_two()
    while(running):
        print(battle_zone.team_battle())
        i = input("do you want to play again(yes/no): ")
        if(i == "no"):
            running = False
        else:
            battle_zone = Arena(int(input("How many heroes does your team have?: ")))
            running = True
            battle_zone.build_team_one()
            battle_zone.build_team_two()
