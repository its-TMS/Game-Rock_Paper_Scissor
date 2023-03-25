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

import random

image = [rock, paper, scissors]
human = int(input("What do you choose? Type '0' for Rock, '1' for Paper, '2' for Scissors.\n"))

if human < 0 or human >= 3:
  print("You chose invalid number, you lose!")

else:
  print(image[human])
    
  bot = random.randint(0,2)
  print(f"\nComputer chose:\n {image[bot]}")
  
  if human == bot:
    print("It's draw!")
  elif human == 0 and bot == 1:
    print("You lost!")
  elif human == 0 and bot == 2:
    print("You won!")
  elif human == 1 and bot == 0:
    print("You won!")
  elif human == 1 and bot == 2:
    print("You lost!")
  elif human == 2 and bot == 0:
    print("You lost!")
  elif human == 2 and bot == 1:
    print("You won!")
