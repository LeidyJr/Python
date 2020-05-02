

# Python3 program to find given  
# two array are equal or not 
  
# Returns true if arr1[0..n-1] and  
# arr2[0..m-1] contain same elements. 
def arrayUnion(arr1, arr2, arr3, n, m): 
  

    if (len(arr3)!=n+m): 
        return False; 

    for i in range(len(arr1)):
    	for j in range(len(arr2)):
    		if arr1[i] and arr2[j] in arr3:
    			return True
    		else:
    			return False
 
# Arreglos
arr1=[4,1,2]
arr2=[7]
arr3=[4,1,7,2]

n = len(arr1); 
m = len(arr2); 
  
if (arrayUnion(arr1, arr2, arr3, n, m)): 
    print("Yes"); 
else: 
    print("No"); 
