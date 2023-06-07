
def fib(max):
    sum = 0
    z = 0 
    x = 0
    y = 1
    
    while x <= max:
        if x % 2 != 0:
            sum += x
        z = x + y
        x = y
        y = z
    return sum
a = input("Hello, AI at your service,\n what your maximum number???")
b = fib(int(a))

print("The sum of your numbers that are odd sir, is,\n %s" % b)

