#include <stdio.h>

int lt(int x,int y) {
    if (x < y){
        return 1;
    }
    
    return -1;
    
}



int gt(int x,int y) {
    if (x > y){
        return 1;
    }
    
    return -1;
    
}

int bs(int *x,int size,int (*compare)(int x,int y)) {
    int i = 0;
    int swapped = 1;
    int temp = -1;
    while (swapped == 1){
        swapped = 0;
        for (i=0;i<size-1;i++){
            
            if (compare(x[i],x[i+1]) == 1){
                temp = x[i];
                x[i] = x[i+1];
                x[i+1] = temp;
                swapped = 1;
            }
        }
    }
    return 1;
}


int main(void) {
   int i=0;
   int vals[10];
   for (i=0;i<10;i=i+1){
      vals[i]=100-i;
   }
   for (i=0;i<10;i++){
      printf("in[%d]=%d\n",i,vals[i]);
   }
   /* HERE: call bs() with the appropriate comparison function */
   for (i=0;i<10;i++){
      printf("out[%d]=%d\n",i,vals[i]);
   }
   return 0;
}

