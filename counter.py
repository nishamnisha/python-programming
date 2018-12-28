def function(st): 
    global MAX
    l = len(st) 
      
    count1, count2 = [0]*MAX, [0]*MAX
      
    for i in range(l//2): 
        count1[ord(st[i]) - ord('a')] += 1
  
    for i in range(l//2, l): 
        count2[ord(st[i]) - ord('a')] += 1
  
    for i in range(MAX): 
        if (count2[i] != count1[i]): 
            return True
  
    return False
 
st = "abcasdsabcae"
if function(st): print("Yes, both halves differ by at least one character") 
else: print("No, both halves do not differ at all") 
