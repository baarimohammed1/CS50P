# prompt user for input
str = input("What is the Answer to the Great Question of Life, The Universe, and Everything? ")
str = str.lower().strip()
match str:
    case "forty two" | "forty-two" | "42":
        print("Yes")
    case _ :
        print("No")