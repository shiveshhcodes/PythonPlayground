# this is going to be my first project excersise in python!! And i made this
# rock paper scissior game here :)

import random

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissor"]
    return random.choice(choices)

def who_the_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie" 
    elif user_choice == "Rock":
        if computer_choice == "Paper":
            return "Computer wins, paper will grab the rock"
        else:
            return "You win, rock will break the scissor"
    elif user_choice == "Scissor":
        if computer_choice == "Paper":
            return "You win, scissor will cut the paper"
        else:
            return "Computer wins, rock will break the scissor"
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            return "You win, paper will grab the rock. hahaha"
        else:
            return "Computer wins, scissor will cut the paper"

def main():
    user_score = 0
    computer_score = 0
    
    for i in range(3):  # Three chances
        user_choice = input("Enter your choice (Rock/Paper/Scissor): ").capitalize()
        while user_choice not in ["Rock", "Paper", "Scissor"]:
            print("Invalid choice! Please enter Rock, Paper, or Scissor")
            user_choice = input("Enter your choice (Rock/Paper/Scissor): ").capitalize()

        computer_choice = get_computer_choice()

        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)

        result = who_the_winner(user_choice, computer_choice)
        print(result)

        if "You" in result:
            user_score += 1
        elif "tie" not in result:
            computer_score += 1

    print("\nFinal Scores:")
    print("Your score:", user_score)
    print("Computer's score:", computer_score)

    if user_score > computer_score:
        print("Congratulations! You win the game")
    elif user_score < computer_score:
        print("Computer wins the game.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
