import sys
import random

while True:
    try:
        level = input("Level: ")
        level = int(level)
        if level >= 1:
            break
        else:
            pass
    except (KeyError, ValueError):
        pass

random = random.randint(1,level+1)

while True:
    try:
        level = input("guess: ")
        guess = int(level)
        if guess == random:
            print("Just right!")
            break
        elif guess < random:
            print("Too small!")
            pass
        elif guess >random:
            print("Too large!")
            pass
    except (KeyError, ValueError):
        pass

