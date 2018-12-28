def round( n ): 
  
  
    m = (n // 7) * 7
      
  
    b = m + 7
      
   
    return (b if n - m > b - n else m) 
  

n = 4722
print(round(n)) 
  
