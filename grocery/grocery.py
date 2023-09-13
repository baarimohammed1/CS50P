d = { }

while True:
    try:
        item = input()
        item = item.upper()
        if item in d:
            d[item] = d[item]+1
        else:
            d[item] = 1
    except EOFError:
        break
    except (KeyError, ValueError):
        pass


for item in sorted(d, key=str.lower):
    print(d[item], item)


