import random
rock = ('''
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
game_list = [rock, paper, scissors]
print(game_list[player_choice])

computer_choice = random.randint(0,2)
print(game_list[computer_choice])

if player_choice >= 3 or player_choice <0:
    print("Chose number from 0, 1 or 2.") 
elif player_choice == 0 and computer_choice == 0:
    print("draw!")
elif player_choice == 0 and computer_choice == 1:
    print("You lose!")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 1 and computer_choice == 0:
    print("You win!")    
elif player_choice == 1 and computer_choice == 1:
    print("draw!")
elif player_choice == 1 and computer_choice == 2:
    print("You lose!")
elif player_choice == 2 and computer_choice == 0:
    print("You lose!")
elif player_choice == 2 and computer_choice == 1:
    print("You win!")
elif player_choice == 2 and computer_choice == 2:
    print("draw!")
