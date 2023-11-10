import random

'''
Plays a game of rock, paper, scissors against a computer opponent.
Player can quit after any game by entering n.
'''

while True:
    # Input asks which option the player would like to play
    player_choice = input("\nType which option you'll play!\n\n1) Rock\n\n2) Paper\n\n3) Scissors\n\n")

    # Computer randomly chooses an option from comp_choices
    comp_choices = ["rock", "paper", "scissors"]
    comp_play = random.choice(comp_choices)

    # Displays what player chose versus what computer chose
    print(f"\nYou chose {player_choice}, and your opponent chose {comp_play}!\n")
    
    # Win/Lose conditions
    # If player and comp chose same options:
    if player_choice == comp_play:
        print(f"Draw! You both played the same call!\n")

    # If player chooses rock:
    elif player_choice.lower() == "rock":
        if comp_play == "scissors":
            print("Rock beats Scissors! You win!\n")
        else:
            print("Paper beats Rock! You lose!\n")

    # If player chooses paper:
    elif player_choice.lower() == "paper":
        if comp_play == "rock":
            print("Paper beats Rock! You win!\n")
        else:
            print("Scissors beats Paper! You lose!\n")

    # If player chooses scissors:
    elif player_choice.lower() == "scissors":
        if comp_play == "paper":
            print("Scissors beats Paper! You win!\n")
        else:
            print("Rock beats Scissors! You lose!\n")

    # After game is over, asks if player would like to play again. N stops code.
    replay = input("\nWould you like to play again? (Y/N): ")
    if replay.lower() != "y":
        break