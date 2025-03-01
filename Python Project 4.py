import random

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_image[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chooses:")
print(game_image[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You have entered a wrong input. YOU LOSE!")
elif user_choice == computer_choice:
    print(f"{YELLOW}It\'s a DRAW!{RESET}")
elif user_choice == 0 and computer_choice == 1:
    print(f"{RED}YOU LOSE!{RESET}")
elif user_choice == 0 and computer_choice == 2:
    print(f"{RED}YOU LOSE!{RESET}")
elif user_choice == 1 and computer_choice == 0:
    print(f"{GREEN}YOU WIN!{RESET}")
elif user_choice == 1 and computer_choice == 2:
    print(f"{RED}YOU LOSE!{RESET}")
elif user_choice == 2 and computer_choice == 0:
    print(f"{RED}YOU LOSE!{RESET}")
elif user_choice == 2 and computer_choice == 1:
    print(f"{RED}YOU LOSE!{RESET}")
