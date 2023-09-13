from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) != 1 and len(sys.argv) !=3:
    sys.exit("Invalid usage")


if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and "--font":
        sys.exit("Invalid usage")
    if sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    else:
        font = sys.argv[2]

if len(sys.argv) == 1:
    font = random.choice(fonts)


figlet.setFont(font=font)
input = input("Input: ")
print("Output:", figlet.renderText(input))
