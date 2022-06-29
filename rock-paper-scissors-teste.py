from random import randint

game = ["rock", "paper", "scissors"]
computer = game[randint(0,2)]
player = False

while player == False:
    player = input("rock, paper, scissors? ")
    if player == computer:
        print("It's a Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("Check your spelling! You must have written it wrong.")

    player = False
    computer = game[randint(0,2)]