import random

print("-----------------------------------------")
print("             GUESS NUMBER APP            ")
print("-----------------------------------------")
num = random.randint(0,100)
guess = int(input("Guess a number between 0 and 100? "))
while (num != guess):
    if (guess < num):
        print("Sorry number {} is LOWER than number.".format(guess))
    else:
        print("Sorry number {} is HIGHER than number.".format(guess))
    guess = int(input("Guess a number between 0 and 100? "))

if (num == guess):
    print("Congratulations, you have got it. The number was {}".format(num))
