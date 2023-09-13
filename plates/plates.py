def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    """
    s = s.lower()
    if len(s) <= 6:
        if s.isalnum():
            if s[0:len(s)].isalpha():
                return True
            i = 0
            while i<= len(s):
                if s[i:len(s)].isnumeric():
                    break
                else:
                    i = i + 1
            if s[0:i].isalpha():
                for c in s[i:7]:
                    if s[i].isalpha():
                        i = i + 1
                    elif s[i] == "0":
                        return False
                    elif s[i:7].isnumeric() :
                        return True
    else: return False
"""
def is_valid(s):
    s = s.lower()
    if len(s) <= 6:
        if s.isalnum():
            if s[0:len(s)].isalpha() and len(s)>3:
                return True
            i = 0
            while i<= len(s):
                if s[i:len(s)].isnumeric():
                    break
                else:
                    i = i + 1
            if s[0:i].isalpha():
                for c in s[i:7]:
                    if s[i].isalpha():
                        i = i + 1
                    elif s[i] == "0":
                        return False
                    elif s[i:7].isnumeric() :
                        return True
            else:
                return False
        else:
            return False
    else:
        return False

main()

