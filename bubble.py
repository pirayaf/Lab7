def printlist(arr):
    for i in range(len(arr)):
        print(arr[i], end="  ")
    print()
    
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp             
    

data = [1,25,-1,0,6]
arr = [1,25,-1,0,6]
print("Array :",end="  ")
printlist(arr)
bubbleSort(data)
print("Sorted Array :",end="  ")
print(data)