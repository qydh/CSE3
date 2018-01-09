import random

# Initializing Variables
answer = random.randint(1, 50)
turns_left = 5
correct_guess = False

# This describes ONE turn (This is the game controller)
while turns_left > 0 and correct_guess is False:
    guess = int(input("Guess a number between 1 and 50: "))

    if guess == answer:
        print("You win!")
        correct_guess = True
    elif guess > answer:
        print("Too high!")
        turns_left -= 1
    elif guess < answer:
        print("Too low!")
        turns_left -= 1
