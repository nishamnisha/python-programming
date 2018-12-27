def isDigitPresent(y, e): 
   
    while (y > 0): 
      
        if (y % 10 == e): 
            break
  
        y = y / 10
       
    return (y > 0) 
  
   
def printNumbers(n, e): 
  

    for i in range(0, n+1): 
  
        if (i == e or isDigitPresent(i, e)): 
            print(i,end=" ") 
   
n = 47
e = 7
print("The number of values are") 
printNumbers(n, e) 
