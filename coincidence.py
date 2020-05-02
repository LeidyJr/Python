def arrayCoincidence(arr1): 

    for i in range(len(arr1)):
        if (arr1[i]==i):
            print(i);
        elif(arr1[i]!=i):
            print(-1);
 
# Arreglos
arr1=[4,1,2]

arrayCoincidence(arr1);