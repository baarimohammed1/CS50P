camel_case = input("camelCase: ")

print("snake_case: ", end="")
for l in camel_case:
    if l.isupper() == True:
        l = l.swapcase()
        print("_" + l, end ="")
    else:
        print(l, end="")
print("")

