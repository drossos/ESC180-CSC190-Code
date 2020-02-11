#include <stdio.h>

struct node{
    struct node *next;
    int val;
};

int main(void){
/*Linked list contains both a pointer to the next node and an int val
 * there fore each node contains 4 + 8 = 12 bytes;
 */
  printf("size of LL is %d",12*100);

}
