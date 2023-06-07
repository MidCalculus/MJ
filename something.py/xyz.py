from winreg import QueryValueEx


money = 1.21
P = 0
N = 0
D = 0
Q = 0
new_money = int(money * 100)
while new_money > 0:
    if new_money >= 25:
        Q = new_money//25 
        new_money = new_money - (25 * Q)
    elif new_money >= 10:
        D = new_money//10
        new_money = new_money - (10 * D)
    elif new_money >=5:
        N = new_money//5
        new_money= new_money-(5 * N)
    else:
        P = new_money//1
        new_money = 0
        break

print("I have", Q, "Quarters, ", D, "Dimes, ", N, "Nickels, ", "and", P, "pennies." )

