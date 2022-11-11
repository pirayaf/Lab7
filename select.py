#Selection Sort
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end="  ")       
        
def SelectionSort(arr,size):
    for step in range(size):
        min_index = step
        for i in range(step + 1, size):       
            if arr[i] < arr[min_index]:
                min_index = i         
            (arr[step], arr[min_index]) = (arr[min_index], arr[step])
arr = [11,4,7,5,10,9,13,1]
data = [11,4,7,5,10,9,13,1]
size = len(data)
print("Array :",end="  ")
printList(arr)
print()
SelectionSort(data,size)
print("Selection Sort Array :",end="  ")
print(data)