#include <stdio.h>
#include <stdlib.h>

struct avlNode {
   int balance; /* -1 Left, 0 balanced, +1 Right */
   int val;
   struct avlNode *l;
   struct avlNode *r;
};

typedef struct avlNode avlNode;

int add_bst(avlNode **root,int val) {
   if (root == NULL) { return -1; }
   if (*root == NULL) {
      *root = (avlNode*)malloc(sizeof(avlNode));
      (**root).val = val;
      (**root).r = NULL;
      (**root).r = NULL;
   } else {
      if ((**root).val < val){
        if ((**root).r == NULL){
            (*root)->r = (avlNode*)malloc(1*sizeof(avlNode));
            (*root)->r->val = val;
            return 0;
      } else {
        return add_bst(&((**root).r),val);
    }
   }else{
       if((**root).l == NULL){
            (**root).l = (avlNode*)malloc(sizeof(avlNode));
            (*root)->l->val = val;
            return 0;
      } else {
        return add_bst(&((**root).l),val);
        }
   }
  }
}

int isAVL(avlNode **root){
    if(root == NULL){return -1;}
    if(*root = NULL){return -1;}
    int rdeep = depth((*root)->r);
    int ldeep = depth((*root)->l);
    if (abs(ldeep - rdeep)>1){
        return -1;
    } else {
        return 0;
    }
}

int depth(avlNode *root){
    if(root == NULL){
        return 0;
    } else {
        int ldepth = 1;
        int rdepth = 1;
        ldepth = ldepth + depth(root->l);
        rdepth = rdepth + depth(root->r);
        if (ldepth > rdepth){
            return ldepth;
        } else {
            return rdepth;
        }
    }
}

int checkBalance(avlNode *root){
    
    if ((root)->l == NULL && (root)->r == NULL){
        (root)->balance = 0;
        return 1;  
    }
    else if ((root)->l == NULL){
        (root)->balance = checkBalance((root)->r);
        return (root)->balance;  
    }
    else if ((root)->r == NULL){
        (root)->balance = -checkBalance((root)->l);
        return (root)->balance;  
    }else{
        (root)->balance = checkBalance((root)->r) - checkBalance((root)->l);
        return (root)-> balance;
    }
}

int main(void){
   avlNode *root=NULL;
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
