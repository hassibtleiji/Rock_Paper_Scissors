import random

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


user_choice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 of Scissors.\n")

if user_choice == '0':
    user_choice = rock
elif user_choice == '1':
    user_choice = paper
else:
    user_choice = scissors

print(user_choice)

comp_choice = random.randint(0, 2)
if comp_choice == 0:
    comp_choice = rock
elif comp_choice == 1:
    comp_choice = paper
else:
    comp_choice = scissors

print(f"Computer chose: {comp_choice}")


if user_choice == rock and comp_choice == paper:
    print("You lose! Try Again.")
elif user_choice == rock and comp_choice == scissors:
    print("You Win!")
elif user_choice == paper and comp_choice == scissors:
    print("You lose! Try Again.")
elif user_choice == paper and comp_choice == rock:
    print("You Win!")
elif user_choice == scissors and comp_choice == rock:
    print("You lose! Try Again.")
elif user_choice == scissors and comp_choice == paper:
    print("You Win!")
else:
    print("Tie Game!")
