import random
import os

def roll_die(sides, advantage: bool = False):
    """Prints the die's results and whether advantage was had"""
    chosen_value = random.randint(1, sides)
    if advantage:
        value_2 = random.randint(1, int(sides))
        chosen_value = max(chosen_value, value_2)
        print("With advantages, ", end="")
    print(f"Player rolled a(n) {chosen_value}\n")
    
roll_die(6, True)
roll_die(8, False)
roll_die(20, True)
what_to_do = ['', '']
advantages_or_not = ""
while(advantages_or_not.casefold() != 'q' ):
    advantages_or_not = input("Do you have advantages (y/n)? Or type 'q' to quit: ").strip()
    while(advantages_or_not.casefold() != 'y' and advantages_or_not.casefold() != 'n' and advantages_or_not.casefold() != 'q'):
        advantages_or_not = input("Invalid input! Do you have advantages (y/n)? Or type 'q' to quit: ").strip()
        
    if(advantages_or_not.casefold() != 'q'):#This line is not reading q correctly and I do not know why.
        what_to_do[1] = advantages_or_not == 'y'
        try:
            what_to_do[0] = int(input("What sided die would you like to roll? ").strip())
        except:
            print("Please only enter numbers...")
            continue
        os.system('cls')
        roll_die(what_to_do[0], what_to_do[1])