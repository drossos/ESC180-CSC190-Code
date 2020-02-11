int fil(float* matrixIn, int rows, int cols, float** matrixOut){
    int i=0;
    int j=0;
    if (matrixIn == NULL){
        return -1;
    } else if(matrixOut == NULL){
        return -1;
    }
    
    matrixOut = (int **)malloc(sizeof(int*)*rows);
    
    for (i=0; i < rows;i++){
        matrixOut[i] = (int *)malloc(sizeof(int)*cols);
    }

    for (i=0; i < rows;i++){
        for (j=0;j<cols;j++){
            if (matrixIn[i][j] < 0){
                *matrixOut[i][j] = 0;
            } else {
                *matrixOut[i][j] = matrixIn[i][j]
            }
        }
    }
    return 0;
}   
