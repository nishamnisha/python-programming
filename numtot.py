a=int(input("Enter a number:"))
tot=0
while(a>0):
    dig=a%10
    tot=tot+dig
    a=a//10
print("The total sum of digits is:",tot)
