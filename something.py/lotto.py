import random

ask = input("how many sets of numbers do you want to pick?")
count = 0

while count < int(ask):
    count += 1
    base = random.randint(1, 45)
    lotto = []
    lotto.append(base)

    while len(lotto) < 7:
        a = random.randint(1, 45)
        if a in lotto:
            pass
        else:
            lotto.append(a)
    
    print(lotto)




