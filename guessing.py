print "Hello! Welcome to the Guessing Game!"
name = raw_input("What is your name?: ")
print "Hello {}".format(name)
import random

def guessing_game():
    number = random.randrange(1, 101)

    guess = 0
    score = 0

    while guess != number:
        try:
            guess = int(raw_input("Pick a number between 1 and 100: "))
            if guess > 0 and guess < 101:
                if guess < number:
                    score += 1
                    print "Guess is too low"                    
                elif guess > number:
                    score += 1
                    print "Guess is too high"                    
                else:
                    score += 1
                    print "Congrats! It took you {0} tries".format(score)
                    restart = raw_input("Would you like to play a new game? Y or N: ")
                    if restart.lower() == "n":
                        break
                    elif restart.lower() == "y":
                        return guessing_game()
                    else:
                        print "Invalid input."
                        break
            else:
                print "Guess is out of range. Try again."
        except ValueError:
            print "Oops! That was not a valid number. Try again."


guessing_game()