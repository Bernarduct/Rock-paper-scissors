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
images = [rock, paper, scissors]
user_choice = int(input("Write 0 for Rock, 1 for paper, 2 for Scissors."))
if user_choice >= 3: 
  print("Your entry is invalid.")
else:
  print(images[user_choice])

computer_choice = random.randint(0,2)
print(f"The computer chose, {computer_choice}")
print(images[computer_choice])
if user_choice ==0 and computer_choice ==2:
  print ("You win.")
elif computer_choice == 0 and user_choice == 2:
  print ("You lose.")
elif computer_choice > user_choice:
  print ("You lose.")
elif user_choice > computer_choice:
  print ("You win.")

elif computer_choice == user_choice:
  print ("it is a draw.")
  