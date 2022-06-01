
import random

while True:
    possible_options = ["rock", "paper", "scissors"] 
    cpu_choice = random.choice(possible_options)
    player_choice = input("Pick your choice (rock, paper, scissors): ")

    Computer = "Computer"
    Player = "Player"

    while player_choice not in possible_options:
        player_choice = input("Invalid! Pick your choice (rock, paper, scissors): ")

    #User choice vs CPU choice 
    print(f"Player ({player_choice}) vs Computer ({cpu_choice})")

    if player_choice == cpu_choice:
        print("Its a tie!")
        #player_choice = input("Pick your choice (rock, paper, scissors): ")
        #exit()

    elif player_choice == "rock":
        if cpu_choice == "scissors":
            print(f"Rock smashes scissors! {Player} wins!")
            #exit()
        else: 
            print(f"Paper covers rock! {Computer} wins!")

    elif player_choice == "paper":
        if cpu_choice == "rock":
            print(f"Paper cover rock! {Player} wins!")
            #exit()
        else:
            print(f"Scissors cuts paper! {Computer} wins!")

    elif player_choice == "scissors":
        if cpu_choice == "paper":
            print(f"Scissors cuts paper! {Player} wins!")
            #exit()
        else:
            print(f"Rock smashes scissors! {Computer} wins!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
