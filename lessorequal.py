def isPrime(m): 
      
    if m <= 1 : 
        return False
  
    for i in range(2, m): 
        if m % i == 0: 
            return False
  
    return True
 
def printPrime(m): 
    for i in range(2, m + 1): 
        if isPrime(i): 
            print(i, end = " ")
if __name__ == "__main__" : 
    m = 7
    
    printPrime(m) 
