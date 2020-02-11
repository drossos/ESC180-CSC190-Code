#include <stdio.h>

int bubbleSort(int *arr, int size);

int bubbleSort(int *arr, int size){
    int swap = 1;
    int i = 0;
    
    if (arr == NULL){
        return -1;
    }
    while (swap == 1){
        swap = 0;
        for (i=1;i<size;i++){
            if (arr[i-1] > arr[i]){
                int temp = arr[i-1];
                arr[i-1] = arr[i];
                arr[i] = temp;
                swap = 1;
            }
        }
    }
    return 0;
}
