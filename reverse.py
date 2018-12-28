def reverse(x): 
    return x[::-1] 
  
def isPalindrome(x): 
   
    rev = reverse(x) 
  
 
    if (x == rev): 
        return True
    return False
  
  

x = "malayalam"
ans = isPalindrome(x) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No") 
