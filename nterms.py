nterms=10
num1 = 0
num2 = 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(num1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(num1,end=' , ')
       nth = num1 + num2
       num1 = num2
       num2 = nth
       count += 1
