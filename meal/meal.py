def main():
    time = input("What time is it? ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes)
    minutes = minutes / 60
    minutes = str(minutes)
    time = float
    new_time = float(hours) + float(minutes)
    return (new_time)

if __name__ == "__main__":
    main()