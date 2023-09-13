def main():
    x = get_fuel("Fraction: ")
    if x >= 99:
        print("F")
    elif x <= 1:
        print("E")
    else:
        print( x, "%", sep="" )

def get_fuel(prompt):
    while True:
        try:
            fraction = input(prompt)
            x, y= fraction.split("/")
            decimal = int(x) / int(y)
            decimal = int((round(decimal, 2)) * 100)
            if decimal > 100:
                continue
            return decimal
        except (ValueError, ZeroDivisionError):
            pass


main()
