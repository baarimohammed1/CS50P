
from validator_collection import validators, checkers, errors

input = input("What's your email?")

if check := checkers.is_email(input):
    print("Valid")
else: print("Invalid")