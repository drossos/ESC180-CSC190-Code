def insertionSort(arr,modVal): 
    divVal = modVal/10
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = (arr[i] % modVal)/divVal 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < (arr[j]%modVal)/divVal : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 


def radix(arr):
    
    for i in range(1,100):
        insertionSort(arr,10*i)

    return arr
