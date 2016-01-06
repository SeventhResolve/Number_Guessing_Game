print "Hello! Welcome to the Guessing Game!"
name = raw_input("What is your name?: ")
print "Hello {}".format(name)
import random
number = random.randrange(1, 101)

guess = 0

while guess != number:
    try:
        guess = int(raw_input("Pick a number between 1 and 100: "))
        if guess < number:
            print "Guess is too low"
        elif guess > number:
            print "Guess is too high"
        else:
            print "Congrats!"
    except ValueError:
        print "Oops! That was not a valid number. Try again."
    