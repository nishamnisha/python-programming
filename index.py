def reorder(arr,index, num):
 
    temp = [0] * num;
 
    
       
    for i in range(0,num):
        temp[index[i]] = arr[i]
 
   
    for i in range(0,num):
        arr[i] = temp[i]
        index[i] = i
     

arr = [50, 40, 70, 60, 90]
index = [3, 0, 4, 1, 2]
num = len(arr)
 
reorder(arr, index, num)
 
print("Reordered array is:")
for i in range(0,num):
    print(arr[i],end = " ")
 
print("\nModified Index array is:")
for i in range(0,num):
    print(index[i],end = " ")
