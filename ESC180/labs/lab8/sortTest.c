#include <stdio.h>
#include "sort.c"

int arrPrint(int *arr, int size);

int arrPrint(int *arr, int size){
    int i;
    for (i=0; i<size;i++){
        printf("%d ",arr[i]);
    }      
}

int main(void){
    int test[] = {5,2,3,4,1};
        
    arrPrint(test, 5);
    bubbleSort(test, 5);
    arrPrint(test, 5);   
    
}
