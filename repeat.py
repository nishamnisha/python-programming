def binarySearch(arr, low, high, z): 
  
    if (high >= low): 
      
        mid = low + (high - low)//2
        if z == arr[mid]: 
            return (mid) 
        elif(z > arr[mid]): 
            return binarySearch(arr, (mid + 1), high, z) 
        else: 
            return binarySearch(arr, low, (mid -1), z) 
      
    return -1
  
    
def countPairsWithDiffK(arr, n, k): 
  
    count = 0
    arr.sort()
 
  
     
    for i in range (0, n - 2): 
        if (binarySearch(arr, i + 1, n - 1,  
                         arr[i] + k) != -1): 
            count += 1
                  
  
    return count 
 
arr= [1, 5, 3, 4, 2] 
n = len(arr) 
k = 3
print ("Count of pairs with given diff is ", 
             countPairsWithDiffK(arr, n, k))  
