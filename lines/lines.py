import sys

#correct num of command-lin arg
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

#command-line arg is a python file
if sys.argv[1].endswith(".py"):
    try:
        with open(sys.argv[1]) as file:
            pass
    except(FileNotFoundError):
        sys.exit("File does not exist")
else:
    sys.exit("Not a Python file")

i = 0
with open (sys.argv[1]) as file:
    for line in file:
        if line.strip():
            if line.strip().startswith("#"):
                pass
            else:
                i = i + 1
print(i)
