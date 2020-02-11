#include <stdio.h>
#include <stdlib.h>

struct bstNode {
   int val;
   struct bstNode *l;
   struct bstNode *r;
};

typedef struct bstNode bstNode;

int add_bst(bstNode **root,int val) {
   if (root == NULL) { return -1; }
   if (*root == NULL) {
      *root = (bstNode*)malloc(sizeof(bstNode));
      (**root).val = val;
      (**root).r = NULL;
      (**root).r = NULL;
   } else {
      if ((**root).val < val){
        if ((**root).r == NULL){
            (*root)->r = (bstNode*)malloc(1*sizeof(bstNode));
            (*root)->r->val = val;
            return 0;
      } else {
        return add_bst(&((**root).r),val);
    }
   }else{
       if((**root).l == NULL){
            (**root).l = (bstNode*)malloc(sizeof(bstNode));
            (*root)->l->val = val;
            return 0;
      } else {
        return add_bst(&((**root).l),val);
        }
   }
  }
}

int printTreeInOrder(bstNode *root){
    
    if ((*root).r == NULL && (*root).l == NULL){
        printf("%d\n",(*root).val);
    } else if ((*root).r == NULL){
        printTreeInOrder((*root).l);
        printf("%d\n",(*root).val);
    } else if ((*root).l == NULL){
        printf("%d\n",(*root).val);
        printTreeInOrder((*root).r);
    } else {
        printTreeInOrder((*root).l);
        printf("%d\n",(*root).val);
        printTreeInOrder((*root).r);
    }
    return 0;
}

int main(void) {
   int n=0;
   int value=0;
   int rvalue=0;
   bstNode *root=NULL;

   while (scanf("%d",&value) != EOF) {
      n=n+1;
      add_bst(&root,value);
   }
   printTreeInOrder(root);

   return 0;
}

