import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if validated_ip := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip):
        for i in [1,2,3,4]:
            if int(validated_ip.group(i)) >=256:
                return False
        return True
    return False



if __name__ == "__main__":
    main()