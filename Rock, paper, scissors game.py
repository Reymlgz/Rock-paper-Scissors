import random

while True:
    choices =["rock","paper","scissors"]

    computer = random.choice(choices)

    player = None

    while player not in choices: #not in no es igual al != el diferente
        player = input("rock, paper or scissors?: ").lower()
        if player not in choices:
            print("Try Again!")

    if player == computer:
        print("computer: ", computer)
        print("player: ",player)
        print("Tie")
    elif player == "rock":
        if computer =="paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You Lose")
        if computer =="scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You Win")
    elif player == "scissors":
        if computer =="paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You Win")
        if computer =="rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You Lose")
    elif player == "paper":
        if computer =="rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You Win")
        if computer =="scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You Lose")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("See you!")