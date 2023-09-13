import sys
import csv

#correct num of command-lin arg
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

#command-line arg is a csv file
if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
    try:
        with open(sys.argv[1]) as file:
            pass
    except(FileNotFoundError):
        sys.exit(f"Could not read {sys.argv[1]}")
else:
    sys.exit("Not a CSV file")

#read before file
students = []
with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        last_name, first_name = row["name"].lstrip().split(",")
        house = row["house"]
        students.append({"first": first_name.strip(), "last": last_name.strip(), "house":house.strip()})



#write new file
with open(sys.argv[2], "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["first","last","house"])
    writer.writeheader()
    for student in students:
        writer.writerow(student)


