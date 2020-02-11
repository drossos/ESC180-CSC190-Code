int histogram(int *n, struct*m,int s){
    int i=0;
    int j=0;
    int searchVal;
    int mInd =0;
    int* used = (int*)malloc(sizeof(int)*s);
    while(1){
        
        for (i=0; i <s;i++){
            if (found(n[i], used,s) != 0){
                searchVal = m[i];
                n[i].value = searchVal;
                used[mInd] = searchVal;
                n[i].valid = 1;
            }
            for (j=0; j<s;j++){
                if (n[j] == searchVal){
                    m[mInd].frequency++;
                }
            }
            mInd++;
        }
        return 0;
    }
}   

int found(int n, int*used, int s){
    int i=0;
    for (i=0;i<s;i++){
        if (used[i] == n){
            return 1;
    }
    return 0;
}
