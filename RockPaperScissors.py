import random
def playgame():
    choices = ["rock", "paper", "scissors"]
    computerchoice = random.choice(choices)
    playerchoice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while playerchoice not in choices:
        playerchoice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    if computerchoice == playerchoice:
        print("TIE!!! :)")
    elif (playerchoice == "rock" and computerchoice == "scissors") or \
         (playerchoice == "paper" and computerchoice == "rock") or \
         (playerchoice == "scissors" and computerchoice == "paper"):
        print("YOU WIN!!! 67676767")
    else:
        print("OOPS YOU LOST :(")
playgame()
