def main():
    fraction = input("Fraction: ")
    x = convert(fraction)
    print(gauge(x))


def convert(fraction):
    x, y= fraction.split("/")
    if x.isdigit() is False or y.isdigit() is False:
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    decimal = int(x) / int(y)
    decimal = int((round(decimal, 2)) * 100)
    return decimal

def gauge(percentage):
    if percentage >= 99:
        return ("F")
    elif percentage <= 1:
        return("E")
    else:
        return ( str(percentage) + "%" )


if __name__ == "__main__":
    main()
