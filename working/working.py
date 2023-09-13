import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    conversions={
    "12:00 AM":"00:",
    "1:00 AM": "01:",
    "2:00 AM": "02:",
    "3:00 AM": "03:",
    "4:00 AM": "04:",
    "5:00 AM": "05:",
    "6:00 AM": "06:",
    "7:00 AM": "07:",
    "8:00 AM": "08:",
    "9:00 AM": "09:",
    "10:00 AM": "10:",
    "11:00 AM": "11:",
    "12:00 PM": "12:",
    "1:00 PM": "13:",
    "2:00 PM": "14:",
    "3:00 PM": "15:",
    "4:00 PM": "16:",
    "5:00 PM": "17:",
    "6:00 PM": "18:",
    "7:00 PM": "19:",
    "8:00 PM": "20:",
    "9:00 PM": "21:",
    "10:00 PM": "22:",
    "11:00 PM": "23:"
}
    if time := re.search("([0-9]?[0-9]):?([0-9]?[0-9]?) (AM|PM) to ([0-9]?[0-9]):?([0-9]?[0-9]?) (AM|PM)",s):
        if not 1 <= int(time.group(1)) <=12 :
            raise ValueError
        if not 1 <= int(time.group(4)) <=12 :
            raise ValueError
        if time.group(2) != "":
            if not 00 <= int(time.group(2)) < 60 :
                raise ValueError
        if time.group(5) != "":
            if not 00 <= int(time.group(5)) < 60 :
                raise ValueError
        if time.group(5) == "" and time.group(2) == "":
            start_time = (f"{time.group(1)}:00 {time.group(3)}")
            end_time = (f"{time.group(4)}:00 {time.group(6)}")

        if time.group(5) != "" and time.group(2) != "":
            start_time = (f"{time.group(1)}:00 {time.group(3)}")
            end_time = (f"{time.group(4)}:00 {time.group(6)}")

        if start_time in conversions:
            new_start_time = conversions[start_time]

        if end_time in conversions:
            new_end_time = conversions[end_time]

        if time.group(5) == "" and time.group(2) == "":
            final_start_time = (f"{new_start_time}00")
            final_end_time = (f"{new_end_time}00")

        if time.group(5) != "" and time.group(2) != "":
            final_start_time = (f"{new_start_time}{time.group(2)}")
            final_end_time = (f"{new_end_time}{time.group(5)}")



        return (f"{final_start_time} to {final_end_time}")
    else: raise ValueError


if __name__ == "__main__":
    main()