money = 120
cans_of_coffee = 0
while money >0:
    if  (money -5) >= 0 and cans_of_coffee < 10:
        print("Coffee purchased")
        money -= 5
        cans_of_coffee += 1
    elif cans_of_coffee == 10:
        print("STOP BUYING VODKA... I MEAN COFFEE")
        break
    else:
        print("Not enough money")
        break






