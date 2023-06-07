input("How was your experience here?")
print("Thank you")
serv_lvl =0
six_people = 0


def tip(six_people, serv_lvl):
    if six_people == 0:
            tip = 15
    else:
            tip = 20
    if serv_lvl == 2:
        tip += 3
    elif serv_lvl == 0:
        tip -= -3

    return (tip/100)


bill = 20.00
num_people = 1
service = 2
serv_lvl = 2
tip_p = bill * tip(num_people, service)
print("Bill: $", bill)
print("Your tip: $", round(tip_p, 2))
print("Total: &", bill+tip_p)