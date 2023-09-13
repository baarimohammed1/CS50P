total = 0
while total < 50:
    inserted_coin = input("Insert Coin: ")
    inserted_coin = int(inserted_coin)
    if inserted_coin == 25 or inserted_coin == 10 or inserted_coin == 5:
        total = total + int(inserted_coin)
    if total >= 50:
        change_owed = total-50
        print("Change Owed:", change_owed)
    else:
        amount_due = 50 - total
        print("Amount Due:", amount_due)

