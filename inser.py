# Insertion sort in Python

def printlist(arr):
    for i in range(len(arr)):
        print(arr[i], end="  ")
    print()
    
def insertionSort(arr):

    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
             
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        
        
        arr[j + 1] = key


data = [1,25,-1,0,6]
arr = [1,25,-1,0,6]
print("Array :",end="  ")
printlist(arr)
insertionSort(data)
print("Insertion sort :",end="  ")
print(data)
