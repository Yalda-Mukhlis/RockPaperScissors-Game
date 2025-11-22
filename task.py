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

rps = [rock, paper, scissors]

# --- Get user choice ---
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))

if user_choice < 0 or user_choice > 2:
    print("Invalid choice! Please enter 0, 1 or 2.")
    exit()

print("You chose:")
print(rps[user_choice])

# --- Computer random choice ---
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(rps[computer_choice])

# --- Game logic ---
if user_choice == computer_choice:
    print("It's a draw 🤝")
elif user_choice == 0 and computer_choice == 2:
    print("You win 🎉 Rock beats Scissors!")
elif user_choice == 2 and computer_choice == 1:
    print("You win 🎉 Scissors cut Paper!")
elif user_choice == 1 and computer_choice == 0:
    print("You win 🎉 Paper covers Rock!")
else:
    print("You lose 😢")
