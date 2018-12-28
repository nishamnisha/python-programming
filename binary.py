def binaryPallindrome(num1): 
  
     binary = bin(num1)
     binary = binary[2:]
     return binary == binary[-1::-1] 
   
if __name__ == "__main__": 
    num1 = 9
    print binaryPallindrome(num1) 

