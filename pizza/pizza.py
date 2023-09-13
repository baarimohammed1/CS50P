import sys
from tabulate import tabulate
import csv

#correct num of command-lin arg
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

#command-line arg is a csv file
if sys.argv[1].endswith(".csv"):
    try:
        with open(sys.argv[1]) as file:
            pass
    except(FileNotFoundError):
        sys.exit("File does not exist")
else:
    sys.exit("Not a CSV file")

table =[]
with open (sys.argv[1]) as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        table.append(row)

print(tabulate(table, headers, tablefmt="grid"))



