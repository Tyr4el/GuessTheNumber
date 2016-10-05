import random

if __name__ == '__main__':

    guessesTaken = 0

    print("Hello!  What is your name?")
    myName = input()

    number = random.randint(1, 20)
    print("Well, %s, I am thinking of a number between 1 and 20" % myName)
    print("Guess the number!")
    print("You have 6 tries!")

    while guessesTaken < 6:
        print("Take a guess!")
        guess = input()
        guess = int(guess)

        guessesTaken += 1

        if guess < number:
            print("Your guess was too low.  Try again!")

        if guess > number:
            print("Your guess was too high.  Try again!")

        if guess == number:
            print("That's right %s!  You guessed the number in %d guesses!" % myName, guessesTaken)
            print("The number was %d", number)
            break

    if guess != number:
        print("No, sorry!  The number I was thinking of was %d" % number)
