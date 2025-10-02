"""
WORKFLOW OF PROJECT
1- Input from user (Rock, paper, scissor)
2- Computer choice (computer will choose randomly not conditionally)
3- Result print

CASES:
A- Rock
rock - rock = tie
rock - paper = paper win
rock - scissor = rock win

B- Paper
paper - paper = tie
paper - rock = paper win
paper - scissor = scissor win

C- Scissor
scissor - scissor = tie
scissor - rock = rock win
scissor - paper = scissor win


"""

import random

user_choice = input("Enter your choice (Rock, paper, or scissor) = ").capitalize()
comp_choice = random.choice(["Rock", "Paper", "Scissor"])

print(f"User choice = {user_choice}")
print(f"Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers rock = Computer win")
    else:
        print("Rock smashes scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper = Computer win")
    else:
        print("Paper covers rock, You win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper = You win")
    else:
        print("Rock smashes scissor, Computer win") 
else:
    print("Invalid choice")


