import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    total_um = len(re.findall(r"\b(u|U){1}m\b", s, re.IGNORECASE))
    return total_um


if __name__ == "__main__":
    main()