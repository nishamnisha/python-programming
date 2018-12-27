import math  
def Log2(y): 
    return (math.log10(y) / 
            math.log10(2)); 
   
def isPowerOfTwo(m): 
    return (math.ceil(Log2(m)) == 
            math.floor(Log2(m)))
if(isPowerOfTwo(31)): 
    print("Yes"); 
else: 
    print("No"); 
  
if(isPowerOfTwo(64)): 
    print("Yes"); 
else: 
    print("No"); 
