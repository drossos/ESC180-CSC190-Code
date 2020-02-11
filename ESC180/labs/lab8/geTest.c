#include <stdio.h>
#include "ge.c"
int printA (float* arr, int rows, int cols);
int main(void){
int*a = NULL;

a = [[-1,1],[-1,0],[0,-1],[-1,-2]]
printA(ge_fw(a,4,2))
printA(ge_bw(ge_fw(a,4,2),4,2))

a = [[1,3,2,1],[2,-3,0,-2]]
printA(ge_fw(a,2,4))
printA(ge_bw(ge_fw(a,2,4),2,4))


a = [[1,2,0],[1,3,3],[-1,0,-1],[-3,0,0]]
printA(ge_fw(a,4,3))
printA(ge_bw(ge_fw(a,4,3)),4,3)

}


int printA (float* arr, int rows, int cols){
    int x,y;
    for(x=0;x<rows;x=x+1){
      for(y=0;y<cols;y=y+1){
         printf("%3d ",p[x*cols + y]);
      }
      printf("\n");
   }
   return 0;
}
