def nextPowerOf2(n1): 
    count1 = 0; 
  
    
    if (n1 and not(n1 & (n1 - 1))): 
        return n1 
      
    while( n1 != 0): 
        n1 >>= 1
        count1 += 1
      
    return 1 << count1; 

n1 = 0
print(nextPowerOf2(n1)) 
