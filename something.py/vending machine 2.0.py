money = 57
coffee_purchased = 0
vend_machine = 20

while money >0 and vend_machine >0:
    if  (money -5) >= 0 and (vend_machine - 1) >= 0:
        print("Coffee purchased")
        money -= 5
        coffee_purchased += 1
        vend_machine -= 1
    else:
        print("Not enough money")
        break


print ("I have", coffee_purchased, "cans")

print ("I have", money, "dollars left")

print ("There are", vend_machine, "cans left in the vending machine")

