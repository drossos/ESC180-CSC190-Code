int isPrime(n){
    int i =0; 
    if (n==2){
        return 0;
    } 
    for (i=2; i < n; i++){
        if (n%i == 0){
            return -1;
        }
    }
    return 0;
}

int isPrimeProduct(n){
    int i=0;
    int j=0;
    
    for (i=2; i <n;i++){
        for (j=2; j<n;j++){
            if (isPrime(j) && isPrime(i) && i*j == n){
                return 0;
            }
        }
    }
    return -1;
}

