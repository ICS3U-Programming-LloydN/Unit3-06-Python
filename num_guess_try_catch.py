#!/usr/bin/env python3
# Created by: Lloyd Najac
# Created on: October 26 2022
# This program checks if a user's integer guess matches the random integer
 
 
import random
 
 
def main_game():
    # defining variables.
    max_number = input("What is the highest guessable number?: ")
    guess_number = input("What is your guess? ")
    random_number = random.randint(1, int(max_number))
    # try is used to tell the user they gave invalid input without crashing the program.
    try:
        guess_as_int = int(guess_number)
        print("You entered the integer correctly")
        if guess_number == random_number:
            print("You guessed correctly!")
        else:
            print("The correct number was {}".format(random_number))
            print("You guessed wrong , try again.")
    except:
        print("Invalid input")
    finally:
        print("Thanks for playing !")
 
 
if __name__ == "__main__":
    main_game()
