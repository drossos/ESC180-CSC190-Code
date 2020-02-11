int getmode(struct *m, int *mode, int size){
    int i =0;
    int mFreq = 0;
    if (m == NULL ){
        return -1;
    }

    for (i=0;i<size;i++){
        if (m[i].frequency > mFreq){
            mFreq = m[i].frequency;
            *mode = m[i].value;
        }
    }
    return 0;
}
