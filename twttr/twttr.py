vowels = ["a","e","i","o","u"]

def main():
    input_1 = input("Input: ")
    input_2 = shorten(input_1)
    print("Output:", input_2)


def shorten(word):
    vowels = ["a","e","i","o","u"]
    for letter in word:
        if letter.lower() in vowels:
            word = (word.replace(letter,""))
    return word


if __name__ == "__main__":
    main()