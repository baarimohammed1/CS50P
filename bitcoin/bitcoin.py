import sys
import json
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
elif sys.argv[1].isdigit() == False and isinstance(float(sys.argv[1]), float) == False :
    sys.exit("Command-line argument is not a number")

while True:
    import requests
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        rate = ( o["bpi"]["USD"]["rate"])
        rate = str(rate)
        rate_new = rate.replace(",","")
        answer = float(rate_new) * float(sys.argv[1])
        print(f"${answer:,.4f}")
        break

    except requests.RequestException:
        pass

