import inflect
import sys

p = inflect.engine()

names =[]
while True:
    try:
        name = input("Name: ")
        names.append(name)
        pass
    except EOFError:
        break
    except (KeyError, ValueError):
        pass
names = p.join((names))
print("Adieu, adieu, to", names)
