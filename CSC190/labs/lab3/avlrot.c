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
    int rdeep, ldeep;
    if(root == NULL){return -1;}
    if(*root = NULL){return 0;}
   
    printf("%d",((*root)->val));
    rdeep = depth((*root)->r);
    ldeep = depth((*root)->l);
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

int rotate(avlNode **root, unsigned int Left0_Right1){
    if (root == NULL){return -1;}
    if (Left0_Right1 == 0){
        return rotateL(*root);
    }else{
        return rotateR(*root);
    }
}

int rotateL(avlNode *root){
    avlNode *temp;
    if (root->r == NULL){return 0;};
    temp = root->r;
    root->r = temp->l;
    temp->l = root;
    root = temp;
    return 0;
}   

int rotateR(avlNode *root){
    avlNode *temp;
    if (root->l == NULL){return 0;};
    temp = root->l;
    root->l = temp->r;
    temp->r = root;
    root = temp;
    return 0;
}   

int dblrotate(avlNode **root,unsigned int MajLMinR0_MajRMinL1){
    if (MajLMinR0_MajRMinL1 == 0){
        return majLminR(*root);
    } else {
        return majRminL(*root);
    }
}

int majLminR(avlNode *root){
    if (root->l == NULL){return 0;}
    rotateL(root->l);
    rotateR(root);
    return 0;
}

int majRminL(avlNode *root){
    if (root->r == NULL){return 0;}
    rotateR(root->r);
    rotateL(root);
    return 0;
}

