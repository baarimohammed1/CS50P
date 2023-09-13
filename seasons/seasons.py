from datetime import date
import sys
import re
import operator
import inflect

def main():
    dob = input("Date of Birth: ")
    new_dob = parse(dob)
    f = calculate_mins(new_dob)
    b = convert_to_words(f)
    print(b)


def parse(dob):
    try:
        if d := re.search(r"(^[0-9]{4})-([0-9]{2})-([0-9]{2}$)", dob):
            year = int(d.group(1))
            month = int(d.group(2))
            day = int(d.group(3))
            new_dob = date(year, month, day )
            return new_dob
        else:
            sys.exit()
    except ValueError: sys.exit()

def calculate_mins(new_dob):
    age = operator.sub(date.today(), new_dob)
    days = age.days
    minutes = days * 1440
    return minutes


def convert_to_words(minutes):
    d = inflect.engine()
    minute_words = d.number_to_words(minutes)
    correct_words = minute_words.replace(" and", "")

    return f"{correct_words.capitalize()} minutes"


if __name__ == "__main__":
    main()