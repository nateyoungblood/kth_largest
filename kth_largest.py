
# Find the kth largest element in an unsorted array. 
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# For example, given [3,2,1,5,6,4] and k = 2, return 5.
# Note: You may assume k is always valid, 1 ≤ k ≤ array's length.

arr1=[3,2,1,5,6,4]
k = 2

 

################################################################

def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    print(arr)
    
# mergeSort(arr1)    

##########################################################################
    
def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]      
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1) 
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high: 
        pi = partition(arr, low, high) 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)            
        return(arr)
        
n = len(arr1)        
quickSort(arr1,0,n-1)        

def kth(arr,k): #O(1)
    quickSort(arr,0,n-1)
    print(arr[len(arr)-k])
    
kth(arr1,k)   