float average(float* nums,int size){
    int i= 0;
    float avg=0;
    if (nums == NULL){
        return -1;
    }
    for (i =0; i < size; i++){
        avg += nums[i];
    }
    return avg/size;
}
