int integrate(float *temp, int l){
    int i=0;
    if (temp == NULL){
        return -1;
    }
    for (i=0; i < l;i+=2){
        temp[i] = temp[i] * temp[i+1];
        temp[i+1] = temp[i+1]-1;
    }
    return 0;
}
