num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

print(int(num1) + int(num2))

f = open("save.txt", 'w')
i = 0

while i < 5:
    i += 1
    f.write("this is line %d"%i)

f.close()

cookies = 7
cola = 2

print("I ate {0} cookies today".format(cookies))
print("I ate {0} and {1} cans of colar today.".format(cookies,cola))

print("{0} and {1} cans of cola this morning.".format ("Jerry", cola))