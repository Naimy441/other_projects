# This is a Guess the Number Game!

import random, sys

name = input("What is your name?: ")

if int(sys.argv[1]) >= 1 and int(sys.argv[1]) <= 100:
    secret_num = int(sys.argv[1])
else:
    secret_num = random.randint(1, 100)

print(f"Hi {name}, I just thought of a random number from 1 to 100! Take a guess.")

for guessesTaken in range(1, 10):
    try:
        guess = int(input())
        if guess > secret_num:
            print("That's too high. Try again!")
        elif guess < secret_num:
            print("That's too low. Try again!")
        else:
            print(f"Wow, you got my secret number in {guessesTaken} guesses. Great job!")
            sys.exit()
    except ValueError:
        print("That's not a number! Try again.")

print(f"You didn't get my secret number. HAHA! It was {secret_num}.")
