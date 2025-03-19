#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Mar. 19, 2025
# This program creates a guessing game, prompting to user.

import constants


def main():
    # Get the chosen number from the user.
    chosen_number = int(input("Guess a number between 0 and 9: "))

    # Check if the user chose the correct number.
    if chosen_number == constants.CORRECT_NUM:
        # Displays they got it correct.
        print("You got it!")

    # Check if the user did not choose the correct number.
    if chosen_number != constants.CORRECT_NUM:
        # Displays they got it wrong, and they must try again.
        print("Incorrect, try again!")


if __name__ == "__main__":
    main()
