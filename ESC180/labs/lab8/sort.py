def bubbleSort(array):
    n = len(array)
    if (n == 0):
        return [-1,array]
    swap = True
    
    while (swap):
        swap = False
        for i in range(1,n):
            if (array[i-1]>array[i]):
                temp = array[i-1]
                array[i-1] = array[i]
                array[i] = temp
                swap = True
    return [0, array]

    
