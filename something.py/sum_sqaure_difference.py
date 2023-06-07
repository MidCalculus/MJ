def sum_sqaure(num):
   s1 = sum(x ** 2 for x in range(num+1))
   s2 = sum(y for y in range(num+1))
   s3 = s2 ** 2
   return s3 - s1
a = input("Enter a random number your highness")
print(sum_sqaure(int(a)))