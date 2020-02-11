/*
#include <stdio.h>
 int swap(int *a, int *b);

int main (void){
    int a = 100;
    int b = 20;
    swap(&a,&b);
    printf("a = %d b = %d",a,b);
}
*/
int swap(int *a, int *b){
    int temp = *b;
    *b = *a;
    *a = temp;
    return 1;
}
