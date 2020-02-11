def fibo(n):
    if n < 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fiboL(n):
    arr = []
    for i in range(0,n+1,1):
        arr += [fibo(i)]
    return arr

def redProd(a,b):
    return a*b

def redfibo(n):
    L = fiboL(n)
    prod =1
    
    for i in range(0,len(L),1):
        prod *= L[i] 
    return prod
