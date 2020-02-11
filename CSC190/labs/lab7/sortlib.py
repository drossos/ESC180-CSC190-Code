def selection_sort(u):

    for i in range(0, len(u)):
        lowest = i
        for j in range(i+1, len(u)):
            if (u[j] < u[lowest]):
                lowest = j
        temp = u[i]
        u[i] = u[lowest]
        u[lowest] = temp

    return True

def heapify(u):
    heap = u
   

    for i in range(len(u),-1,-1):
        reheapify(heap,i)
    return True

def reheapify(heap,end):
    grtInd = end
    l = (end * 2) + 1
    r = (end * 2) + 2
    if (l < len(heap) and heap[end] < heap[l]):
        grtInd = l
        maxVal = heap[l]

    if (r < len(heap) and heap[end] < heap[r] and heap[r] > heap[l]):
        grtInd = r

    if end != grtInd:
        heap[end],heap[grtInd] = heap[grtInd],heap[end]
        reheapify(heap, grtInd)


def heap_sort(u):
   heap = u
   heapify(heap)
   sortedArr = []
   while len(heap) > 0:
      sortedArr = [heap[0]]+ sortedArr 
      heap[0] = heap[len(heap)-1]
      heap = heap[0:len(heap)-1]
      reheapify(heap,0)

   u[:]=sortedArr
   return True

def merge_sort(u):
   if len(u)> 1:
       mid = (int)(len(u)/2)
       L = u[:mid]
       R = u[mid:]
       merge_sort(L)
       merge_sort(R)

       i=0
       j=0
       k=0

       while i < len(R) and j < len(L):
           if (R[i] < L[j]):
               u[k] = R[i]
               i+=1
           elif (R[i] > L[j]):
               u[k] = L[j]
               j+=1
           k+=1
        #check for the longer arr
       while j < len(L): 
            u[k] = L[j] 
            j+=1
            k+=1
       while i < len(R): 
            u[k] = R[i] 
            i+=1
            k+=1
        
def quick_sort(u,ini,fin):
   ...
   pIndex = partition(u,ini,fin)
   ...
   return True

def partition(u,ini,fin):
   ...
   return pIndex

v1=[10,9,8,7,6,5,4,3,2,1,0]
v2=[100,1,1000,9,8,7,2,2000,10]
v3=[100,10,1000,9,8,7,2,6,5,2,3,1]

for i in [ v1,v2,v3 ]:
   print("S.S")
   x=list(i)
   selection_sort(x)
   print(x)

   print("Heap")
   x=list(i)
   heapify(x)
   print(x)

   print("HeapS")
   x=list(i)
   heap_sort(x)
   print (x)

   print("Merge")
   x=list(i)
   merge_sort(x)
   print (x)
