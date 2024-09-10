#GAME
import random
print("GAME TIME")
print("ENJOY GAMING EXPERIENCE")
print("HAVE FUN!!!")
print("ROCK-PAPER-SCISSORS")
print()
print("Rock")
print("Paper")
print("Scissors")
play = 0
comp = 0
options = ("rock", "paper", "scissors")
playing = True
print("Enter in lowercase")
while playing:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Choose one: rock, paper, or scissors: ")
    print("Player chose", player)
    print("Computer chose", computer)
    if player == computer:
        print("IT'S A TIE")
    elif (player == "rock" and computer == "paper") or \
         (player == "paper" and computer == "scissors") or \
         (player == "scissors" and computer == "rock"):
        print("COMPUTER WINS")
        comp += 1
    else:
        print("YOU WIN")
        play+= 1
    print("Score - Player:",play)
    print("Score - Computer:",comp)
    again = input("Do you wish to play again (y/n): ")
    if again == 'y':
        playing = True
    else:
        playing=False
print("Player:",play)
print("Computer:",comp)
print("thanks for playing ")
    
