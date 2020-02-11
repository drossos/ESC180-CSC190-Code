def quicksort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quicksort(arr, low, pi-1) 
        quicksort(arr, pi+1, high)

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 


def hanoi(n,start,tmp,final):
   if n > 0:
        hanoi(n - 1, start, final, tmp)
        hanoi(n - 1, tmp , start, final)
        print (start,tmp,final)
        return True
   else:
        print (start,tmp,final)
        return True

