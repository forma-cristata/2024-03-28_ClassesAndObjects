import random
import math
import time


class Monster:
    def __init__(self, name:str, HP:int, attack_stat:int, defense_stat:int, speed_stat:int):
        self.name = name
        self.HP = HP
        self.attack_stat = attack_stat
        self.defense_stat = defense_stat
        self.speed_stat = speed_stat
    
    def take_damage(self, damage_taken:int):
        """Calculates and takes damage from the defending monster's HP"""
        if(random.randint(1, 10) == 1):
            damage_received:int = 2 * (damage_taken - self.defense_stat)
            print(f"{self.name} has sufferred a critical hit!!")
        else:
            damage_received = damage_taken - self.defense_stat
        if(damage_received < 1):
            damage_received = 1
        print(f"{self.name} has taken {damage_received} points of damage!")
        self.HP -= damage_received
    
    def is_knocked_out(self):
        """Returns true if a monster has run out of HP"""
        return (self.HP < 1)
    
class Arena:
    def __init__(self, monster1:Monster, monster2:Monster):
        self.monster1 = monster1
        self.monster2 = monster2
    
    def fight(self):
        """Switches the monster's turns attacking and adds functionality
        to the user experience"""
        print(f"{self.monster1.name} is fighting {self.monster2.name}!")
        i = 1
        print(f"Round {i}...")
        fighter_speed_stat = max(self.monster1.speed_stat, self.monster2.speed_stat)#this is returning the wrong thing
        if fighter_speed_stat == self.monster1.speed_stat:
            fighting_monster = self.monster1
            damaged_monster = self.monster2
        else:
            fighting_monster = self.monster2
            damaged_monster = self.monster1
        print(f"{fighting_monster.name} will attack first... {damaged_monster.name}'s is on the defense!")
        damaged_monster.take_damage(fighting_monster.attack_stat)
        while( not self.monster1.is_knocked_out() and not self.monster2.is_knocked_out()):
            time.sleep(2)
            i += 1
            if(i%2 != 0):
                print(f"\nRound {round(i/2)}...")
            fighting_monster.take_damage(damaged_monster.attack_stat)
            
            temp = fighting_monster
            fighting_monster = damaged_monster
            damaged_monster = temp
        print(f"\n{fighting_monster.name} has been killed by {damaged_monster.name}")
    
    
monsty_1 = Monster("Hellcat", 563, 20, 5, 602)
monsty_2 = Monster("Demon", 610, 23, 6, 1000)
this_fight = Arena(monsty_1, monsty_2)
this_fight.fight()
