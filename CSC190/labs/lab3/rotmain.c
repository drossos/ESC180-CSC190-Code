#include <stdio.h>
#include <stdlib.h>
#include <avlrot.c>

int main(void){
    avlNode *root = NULL;
    add_bst(&root,5);
    add_bst(&root,3);
    add_bst(&root,1);
    add_bst(&root,4);
    add_bst(&root,7);
    add_bst(&root,6);
    add_bst(&root,8);
    printf("%d",isAVL(&root)); 
    return 0;
}
