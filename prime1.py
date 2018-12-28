n1=407
if n1 > 1:
   
   for i in range(2,n1):
       if (n1 % i) == 0:
           print(n1,"is not a prime number")
           print(i,"times",n1//i,"is",n1)
           break
   else:
       print(n1,"is a prime number")
       

else:
   print(n1,"is not a prime number")
