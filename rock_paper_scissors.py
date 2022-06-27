from random import randint
game = ["rock, paper, scissors"]
computer = game[randint(0,2)]
player = False

while player == False:
    player(input("rock, paper or scissors? "))
if player == computer:
print("It's a tie!")
