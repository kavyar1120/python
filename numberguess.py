import random
secret=random.randint(1,100)
guess=None

while guess!=secret:
    guess=int (input("Guess a number between 1 and 100:"))
    if guess<secret:
        print("too low")
    elif guess>secret:
        print("too high")
    elif guess==secret%2==0:
        print("guess is an even number")
print("you got it")