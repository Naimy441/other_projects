import random
from debug import *
config(True)

# Create the Grid
grid = []
GRID_WIDTH = 10
GRID_LENGTH = 10
max_num = GRID_WIDTH*GRID_LENGTH

count = 1
for i in range(GRID_LENGTH):
    row = []
    for j in range(GRID_WIDTH):
        item = str(count).rjust(len(str(max_num)), '0')
        row.append(item)
        count += 1
    grid.append(row)

# Define Functions
def getValidNum(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number < 1 or number > max_num:
                raise Exception()
            return number
        except:
            print(f'Please enter a number that is between 1 and {max_num}.')

# Intialize Variables
num_of_tries = 12
starting_number = int(getValidNum('What is your starting number?: '))
prev_guesses = [starting_number]

secret_number = random.randint(1, max_num)
while secret_number == starting_number:
    secret_number = random.randint(1, max_num)
log(secret_number)

# Game
for i in range(1, num_of_tries+1):
    # Get Guess
    not_unique = True
    guess = getValidNum(f'Guess {i} - Pick a number!: ')
    while not_unique:
        for prev_guess in prev_guesses:
            if guess == prev_guess:
                guess = getValidNum(f'Guess {i} - Don\'t use previous numbers!: ')
                continue
            not_unique = False
    prev_guesses.append(guess)

    # Check Guess
    if guess == secret_number:
        print('You got the number!')
        break

    # Print New Board
    print('\n')
    for x in grid:
        row = ''
        for y in grid:
            index = str(int(grid[grid.index(x)][grid.index(y)]))
            for prev_guess in prev_guesses:
                if index == str(prev_guess):
                    index = '###'
            row += str(index).rjust(len(str(max_num)), '0') + ' '
        print(row + '\n')

    # Check Distances
    snx = None
    sny = None
    prev_distance = None
    distance = None
