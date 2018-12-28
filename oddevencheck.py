def check(m):
    if (m < 2):
        return (m % 2 == 0)
    return (check(m - 2))
m=int(input("Enter number:"))
if(check(m)==True):
      print("Number is even!")
else:
      print("Number is odd!")
