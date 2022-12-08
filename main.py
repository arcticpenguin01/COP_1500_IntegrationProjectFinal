"""Description: This program is a multiplication quiz game. """

__author__ = "Elijah J. Baptiste"

import time  # importing time module
from random import randint  # imports a list of numbers and can perform operations with them found on geeks for geeks

# Welcome screen
print('Hi Im Jarvis, welcome to the multiplication quiz game! ')
time.sleep(1)  # time.sleep() is a function that delays the execution of the next line of code
print("In this game you will be asked multiplication questions of increasing difficulty...")
time.sleep(3)
print("For maximum fun, don't use a calculator!")
time.sleep(3)
continue_game = input('Press ENTER to continue')
name_of_player = input('Enter your name: ')
print("Authenticating...")
time.sleep(3)
are_you_ready = input(f"Welcome {name_of_player}, press ENTER to start the game: ")

# Countdown to start of game
print("Starting game in...")
time.sleep(1)
print("5...")
time.sleep(1)
print("4...")
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("0")
print("Start!!")


# Start of the game : Round 1

def round1():
    """ The purpose of this  function is to ask multiplication questions
     and determine if the user's answer is correct or incorrect. """
    round_condition1 = True
    print('ROUND 1! ')
    while round_condition1:
        for x in range(1, 6):
            first_number = randint(2, 9)  # randomly generates numbers from 2 to 9
            second_number = randint(2, 9)
            product = first_number * second_number  # generates the operations that will be posed to user
            good_input = False
            while not good_input:
                try:
                    user_answer = int(input(f'What is {first_number} * {second_number}? '))
                    answer = int(user_answer)
                    good_input = True
                except ValueError:
                    print("Not an integer. Please enter an integer! ")
            if answer == product:
                print("Awesome! ")
            else:
                print("Incorrect! ")
        round_condition1 = False


round1()


# Round 2
def round2():
    """ The purpose of this  function is to ask multiplication questions
         and determine if the user's answer is correct or incorrect. """
    round_condition2 = True
    print("ROUND 2!")
    while round_condition2:
        for x in range(1, 6):
            second_round_number = randint(2, 10)
            second_round_number2 = randint(2, 10)
            product2 = second_round_number * second_round_number2
            user_input = False
            while not user_input:
                try:
                    user_answer2 = int(input(f'What is {second_round_number} * {second_round_number2}? '))
                    answer2 = int(user_answer2)
                    user_input = True
                except ValueError:
                    print("Not an integer. Please enter an integer! ")
            if product2 == answer2:
                print(f'Keep it up {name_of_player}! ')
            else:
                print("Incorrect! ")
        round_condition2 = False


round2()


def round3():
    """ The purpose of this  function is to ask multiplication questions
         and determine if the user's answer is correct or incorrect. """
    round_condition3 = True
    print("ROUND 3! ")
    while round_condition3:
        for x in range(1, 6):
            third_round_number = randint(2, 11)
            third_round_number2 = randint(2, 11)
            product3 = third_round_number * third_round_number2
            user_input2 = False
            while not user_input2:
                try:
                    user_answer = int(input(f'What is {third_round_number} * {third_round_number2}? '))
                    answer3 = int(user_answer)
                    user_input2 = True
                except ValueError:
                    print("Not an integer. Please enter an integer! ")
            if product3 == answer3:
                print(f'Keep it up {name_of_player}! ')
            else:
                print("Incorrect!")
        round_condition3 = False


round3()


def playNewGame():
    """ The purpose of this function is to give the user
        the option to play the game again. """
    play_again = input("Do you want to pay again? (Y/N)")
    if play_again == "Y":
        round1()
        round2()
        round3()
    else:
        print("Goodbye! ")
        time.sleep(2)
        print("See you again soon! ")


playNewGame()

# Required components
# number != 3   comparison operator. Line is read as "number is not equal to 3".
# number > 3 this is a boolean relational operation, and it reads "number is greater than 3"

# number = 4
# print(number < 1 and number > 4) returns true if both conditions are true (in this case will return False)

# number = 3
# print(number < 1 or number < 4) returns true if either condition is true (in this case will return True)

# number = 3
# print( number == 4) returns true if condition is false ( in this case it will return True)
