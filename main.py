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

#Write your code below this line 👇
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
  print("You entered an invalid number, You Lose")
else:
  print(game_images[user_choice])
  
  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])
  
  if user_choice == 0 and computer_choice == 2:
    print("You Win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You Lose")
  elif computer_choice == user_choice:
    print("It's a draw")
  elif computer_choice > user_choice:
    print("You Lose")
  elif user_choice > computer_choice:
    print("You Win!")
































# import random
# option = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
# computer = random.randint(0,2)

# if computer == option:
#   print("It's a draw")

# if select == "0":
#   print(f"{rock}\n")
# elif select == "1":
#   print(f"{paper}\n")
# elif select == "2":
#   print(f"{scissors}\n")
# else:
#   print("You selected a different option.")

# if computer == select:
#   print("It's a draw")
# elif computer == 1 and select == "1":
#   print(f"Computer Chose:\n {paper}\n It's a draw")

  
# if computer == 0 and select == "0":
#   print(f"Computer Chose:\n {rock}\n It's a draw")
# elif computer == 1 and select == "1":
#   print(f"Computer Chose:\n {paper}\n It's a draw")
# elif computer == 2 and select == "2":
#   print(f"Computer Chose:\n {scissors}\n It's a draw")
# elif select == "1" and computer == 0:
#   print(f"Computer Chose:\n {rock}\n You Win")
# elif select == "0" and computer == 1:
#   print(f"Computer Chose:\n {paper}\n You Lose")
# elif select == "2" and computer == 0:
#   print(f"Computer Chose:\n {rock}\n You Lose")
# elif select == "0" and computer == 2:
#   print(f"Computer Chose:\n {scissors}\n You Win")
# elif select == "1" and computer == 2:
#   print(f"Computer Chose:\n {scissors}\n You Lose")
# elif select == "2" and computer == 1:
#   print(f"Computer Chose:\n {paper}\n You Win")