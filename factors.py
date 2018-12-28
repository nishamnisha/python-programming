def print_factors(x1):
   
   print("The factors of",x1,"are:")
   for i in range(1, x1 + 1):
       if x1 % i == 0:
           print(i)
num = 320
print_factors(num)
