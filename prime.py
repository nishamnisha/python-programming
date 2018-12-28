num1=407
if num1 > 1:
   
   for i in range(2,num1):
       if (num1 % i) == 0:
           print(num1,"is not a prime number")
           print(i,"times",num1//i,"is",num1)
           break
   else:
       print(num1,"is a prime number")
       

else:
   print(num1,"is not a prime number")
