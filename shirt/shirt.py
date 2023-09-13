import sys
import csv
import os
from PIL import Image
import PIL


#correct num of command-lin arg
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

#command-line arg is a correct file and that they match
root_1, ext_1 = os.path.splitext(sys.argv[1])
root_2, ext_2 = os.path.splitext(sys.argv[2])

correct_extensions =[".jpeg",".jpg",".png"]
#correct extension type
if ext_1 not in correct_extensions:
    sys.exit("Invalid output1")

#correct extension type
if ext_2 not in correct_extensions:
    sys.exit("Invalid output2")

#same extension
if ext_1 != ext_2:
    sys.exit("Input and output have different extensions")

#validate input
try:
    with open(sys.argv[1]) as file:
        pass
except(FileNotFoundError):
    sys.exit("Input does not exist")

#open input
input = Image.open(sys.argv[1])
shirt = Image.open("shirt.png")


#resize input to shirt size
size = shirt.size
new = PIL.ImageOps.fit(input, size)

#overlay shirt on new image
new.paste(shirt, shirt)

#save the resulting image
new.save(sys.argv[2])