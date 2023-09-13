def main():
    str = input("Greeting: ").strip()
    print("$",value(str), sep="")

def value(greeting):
    greeting_1 = greeting.lower()
    if greeting_1.startswith("hello"):
        return int(0)
    elif greeting_1.startswith("h"):
        return int(20)
    else: return int(100)

if __name__ == "__main__":
    main()