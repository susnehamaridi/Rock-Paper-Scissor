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


choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("Invalid choice")
print("Computer chose:")
sequence=[rock,paper,scissors]
random_int=random.choice(sequence)
print(random_int)
if random_int == rock:
    if choice == 0:
        print("It's a draw!")
    elif choice == 1:
        print("You win!")
    else:
        print("You lose!")
elif random_int == paper:
    if choice == 0:
        print("You lose!")
    elif choice == 1:
        print("It's a draw!")
    else:
        print("You win!")
elif random_int == scissors:
    if choice == 0:
        print("You win!")
    elif choice == 1:
        print("You lose!")
    else:
        print("It's a draw!")