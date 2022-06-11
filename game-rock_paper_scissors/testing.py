my_list, comp_list = [rock, paper, scissors]
user_choice = input("Enter an option from my_list: ")
from random import choice
comp_choice = random.choice(comp_list)
print("You have chosen {} and the computer has chosen {}".format(user_choice, comp_choice)

if user_choice == comp_choice:
        print("It's a tie!")
elif user_choice == rock:
    if comp_choice == paper:
        print("user wins!")
    else:
        print("computer wins!")
elif user_choice == rock:
    if comp_choice == scissors:
        print("user wins!")
    else:
        print("computer wins!")
elif user_choice == paper:
    if computer_choice == scissors:
        print("computer wins!")
    else:
        print("user wins")

round_2 = input("round 2? (y/n): ")
if round_2 != "y":
    break
