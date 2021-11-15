# Program to build rock, paper, scissor game using python:

import random      # importing random module for computer's choice

######################################

# defining function and checking for all possibilities


def result(comp, user):
    if comp == user:       # if both selected same object
        return None

    elif comp == 'rock':   # if computer selected rock then check for all possibilities
        if user == 's':
            return False
        elif user == 'p':
            return True

    elif comp == 'paper':  # if comp selected paper then checking all possibilities
        if user == 'r':
            return False
        elif user == 's':
            return True

    elif comp == 'scissor':    # if comp selected scissor selected then checkin for all possibilities
        if user == 'p':
            return False
        elif user == 'r':
            return True

##############################################


print("Computer's turn : Selecting........Done!!")

# random module operation for comp selection choice
num = random.randint(1, 3)
if num == 1:
    computer = 'rock'
elif num == 2:
    computer = 'scissor'
elif num == 3:
    computer = 'paper'

###############################################

# taking user input choice
player = input("Player's turn : Please select your choice from Rock(r), Paper(p),Scissor(s) : \n")

if player == 'r':       # printing choices as a word for user ---> eg. r = rock
    u = 'rock'
elif player == 's':
    u = 'scissor'
elif player == 'p':
    u = 'paper'

##############################################


print('########_____The Game___#########')

# printing the choices for both
print('computer selected :', computer)
print('user selected :', u)

############################################


# using above function to declare result of input of both players
winner = result(computer, player)


if winner == None:
    # printing the result of the game by passing booleans from the function
    print('The game is a tie. Play again....')
elif winner == True:
    print('You win.')
else:
    print('You lost.')
