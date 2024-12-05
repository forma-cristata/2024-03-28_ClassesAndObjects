from random import choice

my_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e")
chosen = []

for i in range (0, 4):
    chosen_element = choice(my_tup)
    chosen.append(chosen_element)
    
print("Here are the winning tickets! Come up to collect your prizes: ", end="")
for winner in chosen:
    print(str(winner), end="   ")