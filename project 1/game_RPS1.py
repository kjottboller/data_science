## Rock Paper Scissors game
# here we go

import random
player_wins = 0
computer_wins = 0

while player_wins < 3 and computer_wins < 3:
    
    user = input("Your choice: ")
    computer = random.choice(["Rock", "Paper", "Scissors"])
    
    print("Computer chose: ", computer)
    
    if user == computer:
        print("Same choise")
    elif user == "Rock":
        if computer == "Scissors":
            print("User wins! Rock broke the scissors!")
            player_wins += 1
        else:
            print("Computer wins! Paper covers Rock")
            computer_wins += 1
    
    elif user == "Paper":
        if computer == "Scissors":
            print("Computer wins! Scissors cut a paper")
            computer_wins += 1
        else:
            print("User wins! Paper covers Rock")
            player_wins += 1
    
    elif user == "Scissors":
        if computer == "Paper":
            print("User wins! Scissors cut a paper")
            player_wins += 1
        else:
            print("Computer wins! Rock broke a scissors")
            computer_wins += 1
    
    print("Score: ", player_wins, ":", computer_wins)

if player_wins > computer_wins:
    print("User won this game!")
else:
    print("Computer won this game!")
            
            
            