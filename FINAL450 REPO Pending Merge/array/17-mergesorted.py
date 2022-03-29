import math as m
def mergeSortedExtraSpace(arr1, arr2):
    """
    TC: O(M+N)
    SC: (M+N)
    """
    result = [0] * (len(arr1) + len(arr2)) 
    i, j, k = 0, 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result[k] = arr1[i]
            i+=1
        else:
            result[k] = arr2[j]
            j+=1
        k+=1
    
    while i < len(arr1):
        result[k] = arr1[i]
        i, k = i+1, k+1
    
    while j < len(arr2):
        result[k] = arr2[j]
        j, k = j+1, k+1
    
    return result
            
def mergeSortedWithoutExtraSpace(arr1, arr2, m, n):
    """
    M: size of arr1
    N: size of arr2
    TC: O(M*N)
    """
    i = n-1
    while i >= 0:
        j, last = m-2, arr1[m-1]
        while j >= 0 and arr1[j] > arr2[i]:
            arr1[j+1] = arr1[j]
            j-=1
        if j != m-2 or last > arr2[i]:
            arr1[j+1], arr2[i] = arr2[i], last
        i-=1

def mergeSortedArrayLogrithmic(arr1, arr2, m, n):
    """
    TC: ((M+N)* log(M+N))
    """
    def calculateGap(n):
        if n <= 1:
            return 0
        else:
            return (n//2) + (n%2)
            #alternative Math.Ceil(n/2)
    
    gap = calculateGap(m+n)
    while gap > 0:
        
        i = 0
        #comparing element in array 1
        while i+gap < m:
            if arr1[i] > arr1[i+gap]:
                arr1[i], arr1[i+gap] = arr1[i+gap], arr1[i]
            i+=1
        
        #comparing array in both array
        if gap > m:
            j = gap-m
        else:
            j = 0
        
        while i < m and j < n:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i, j = i+1, j+1

        #comparing in second array
        if j < n:
            j = 0
            while j+gap < n:
                if arr2[j] > arr2[j+gap]:
                    arr2[j], arr2[j+gap] = arr2[j+gap], arr2[j]
                j+=1
        
        #update the gap
        gap = calculateGap(gap)


    
if __name__ == "__main__":
    arr1 = [1,3,5,7]
    arr2 = [0,2,6,8,9]
    print(mergeSortedExtraSpace(arr1,arr2))
    print(arr1)
    print(arr2)
    #mergeSortedWithoutExtraSpace(arr1, arr2, len(arr1), len(arr2))
    mergeSortedArrayLogrithmic(arr1, arr2, len(arr1), len(arr2))
    print(arr1)
    print(arr2)
    

