#include <stdlib.h>

typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
   int (*compare)(int x,int y);
   int (*retrieve)(intHeap_T*, int *rvalue);
   int (*store)(intHeap_T*, int value);
   
} intHeap_T;

int lt(int x,int y) {
    if (x < y){
        return 1;
    }
    
    return -1;
    
}


int store(intHeap_T* heap,int value) {
    return 1;
}
int retrieve(intHeap_T* heap,int *rvalue) {
    *rvalue = heap->store[(heap->size)-1];
    heap->size = heap->size - 1;
    if (heap->size > 0){
        heap->store[0] = heap->store[heap->size + 1];
    }

    return 1;
}


int main(void){
    intHeap_T heap;
    heap.store=(int *)malloc(1000*sizeof(int));
    heap.size=1000;
    heap.end=0; /* empty heap condition; obey this spec */
    heap.compare = lt;
}
