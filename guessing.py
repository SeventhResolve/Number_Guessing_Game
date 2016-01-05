print "Hello! Welcome to the Guessing Game!"
name = raw_input("What is your name?: ")
print "Hello {}".format(name)
number = random.randrange(1, 101)

guess = raw_input("Pick a number between 1 and 100: ")

while guess != number:
    if guess < number:
        print "Guess is too low"
    else print "Guess is too high"

