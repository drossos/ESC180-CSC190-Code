#include <stdio.h>
#include <stdlib.h>

struct bstNode {
   int val;
   struct bstNode *l;
   struct bstNode *r;
};

struct queue {
    struct bstNode *arr;
    int start;
    int end;
};

typedef struct queue queue;
typedef struct bstNode bstNode;

int push (queue *stk, bstNode val){
    stk->arr[stk->end] = val;
    stk->end = stk->end + 1;
}

bstNode pop(queue *stk){
    bstNode temp;
    temp = stk->arr[stk->start -1];
    stk->end = stk->start + 1;
    return temp;
}

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

int printLevelOrder(bstNode *root){
    bstNode temp;
    queue *stk = (queue*)malloc(sizeof(queue));
    stk->arr = (bstNode*)malloc(sizeof(bstNode)*10000);
    push(stk,*root);
    
    while (stk->end != stk->start){
    temp = pop(stk);
    if ((temp).r == NULL && (temp).l == NULL){
        printf("%d ",(temp).val);
    } else if ((temp).r == NULL){
        printf("%d ", (temp).val);
        push(stk,*((temp).l));
        
    } else if ((temp).l == NULL){
       
        printf("%d ", (temp).val);
        push(stk,*((temp).l));
    } else {
        printf("%d ", (temp).val);
        
        push(stk,*((temp).l));
        push(stk,*((temp).r));
    }
    return 0;
    }
}

int main(void) {
   bstNode *root=NULL;
   add_bst(&root,5);
   add_bst(&root,3);
   add_bst(&root,1);
   add_bst(&root,4);
   add_bst(&root,7);
   add_bst(&root,6);
   add_bst(&root,8);
   printTreeInOrder(root);
   printLevelOrder(root);
   return 0;
}
