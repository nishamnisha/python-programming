def round( n1 ): 
  
 
    a = (n1 // 10) * 10
      
   
    b = a + 10
      
    
    return (b if n1 - a > b - n1 else a) 
  

n1 = 4722
print(round(n1)) 
