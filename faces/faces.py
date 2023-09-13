def main():
    # prompt user for input
    str = input()
    #convert
    str = convert(str)
    #print
    print(str)

def convert(str):
    str = str.replace(":)" ,"🙂")
    str = str.replace(":(" ,"🙁")
    return str

main()