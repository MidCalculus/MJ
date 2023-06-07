def cheese():
ans = input("Enter the number: ")
num = int(ans)
calc = 2 ** num
print("Your number was the amount of times two was multiplied by itself \nand the amount was: ", calc)

t = str(calc)

sum = 0
for i in t:
    sum = sum + int(i)


print("This is the sum of the digits in your power: ", sum)

retry = input("Would you like to try again?")
if retry == "yes":