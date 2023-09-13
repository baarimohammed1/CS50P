
def main():
    level = get_level()
    i = 0
    score = 0
    for _ in range(9):

        num1 = generate_integer(level)
        num2 = generate_integer(level)
        answer = num1 + num2
        user_prompt = str(num1) + " " + "+" + " " +str(num2) + " "+ "=" +" "
        i = 0
        while i < 3:
            try:
                user_answer = input(user_prompt)
                if user_answer != str(answer):
                    print("EEE")
                    i += 1
                    if i == 3:
                        print(user_prompt, answer, sep="")
                        pass
                    pass

                elif user_answer == str(answer):
                    score += 1
                    break
            except(KeyError):
                    print("EEE")
                    i += 1
                    pass


    print("Score:", score+1)





def get_level():
    while True:
        try:
            level = input("Level: ")
            level = int(level)
            if 3 >= level >= 1 :
                return level
            else:
                pass
        except (KeyError, ValueError):
            pass


def generate_integer(level):
    import random
    if level == 3:
        random = random.randint(100,999)
        return random
    elif level == 2:
        random = random.randint(10,99)
        return random
    elif level == 1:
        random = random.randint(0,9)
        return random

if __name__ == "__main__":
    main()