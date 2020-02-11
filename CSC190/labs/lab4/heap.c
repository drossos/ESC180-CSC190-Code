#include <stdlib.h>

typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
} HeapType;

typedef struct { 
   int data; 
   int *st;
   int end;    
} Stack; 

int initHeap (HeapType *pHeap,int size){
    if (pHeap == NULL){
        return -1;
    }

    pHeap->size = size;
    pHeap->end = 0;

    pHeap->store = (int *)malloc(size * sizeof(int));

    return 0;
}
/*
Arr[(i-1)/2]    Returns the parent node
Arr[(2*i)+1]    Returns the left child node
Arr[(2*i)+2]    Returns the right child node
*/
int inorder  (HeapType *pHeap, int **output, int *o_size){
    int curr = 0;
    int tempPop = 0;
    *output = (int *)malloc(pHeap->end * sizeof(int));
    int addI = 0;
    Stack *s = NULL;
    s->end = 0;
    s->st = (int *)malloc(1000 * sizeof(int));
    *o_size = pHeap->end;
    
    if (pHeap == NULL){
        return -1;
    }

    while(1){
        push(s,curr);
        
        if(curr < pHeap->end){
            curr = (2*curr)+1;
        } else if (curr >= pHeap->end){
            if (s->end == 0){
                break;
            }else{
                tempPop = pop(s);
                output[addI] = pHeap->store[tempPop];
                curr = (tempPop*2)+2;
                addI++;    
            }   
        }

    }
    return 0;               
}

int preorder (HeapType *pHeap, int **output, int *o_size){
    int curr = 0;
    int tempPop = 0;
    *output = (int *)malloc(pHeap->end * sizeof(int));
    int addI = 0;
    Stack *s = NULL;
    s->end = 0;
    s->st = (int *)malloc(1000 * sizeof(int));
    *o_size = pHeap->end;
    
    if (pHeap == NULL){
        return -1;
    }

    while(1){
        push(s,curr);
        output[addI] = pHeap->store[curr];
        addI++;
        if(curr < pHeap->end){
            curr = (2*curr)+1;
        } else if (curr >= pHeap->end){
            if (s->end == 0){
                break;
            }else{
                tempPop = pop(s);
                curr = (tempPop*2)+2;    
            }   
        }

    }
    return 0;
}               

int postorder(HeapType *pHeap, int **output, int *o_size){
    int curr = 0;
    int tempPop = 0;
    *output = (int *)malloc(pHeap->end * sizeof(int));
    int addI = 0;
    Stack *s = NULL;
    s->end = 0;
    s->st = (int *)malloc(1000 * sizeof(int));
    *o_size = pHeap->end;
    
    if (pHeap == NULL){
        return -1;
    }

    while(1){
        push(s,(curr*2)+2);
        push(s,curr);
        if(curr < pHeap->end){
            curr = (2*curr)+1;
        } else if (curr >= pHeap->end){
            if (s->end == 0){
                break;
            }else{
                tempPop = pop(s);
                curr = (tempPop*2)+2;    
                output[addI] = pHeap->store[(curr-1)/2];
                addI++;
            }   
        }

    }
    return 0;
}               

int addHeap(HeapType *pHeap, int key){
    int ind = 0;  
    int temp = 0; 
    pHeap->store[pHeap->end] = key;
    pHeap->end = pHeap->end +1;
    ind = pHeap->end-1;
    
    while (pHeap->store[ind] < pHeap->store[(ind-1)/2]){
        temp = pHeap->store[ind];
        pHeap->store[ind] = pHeap->store[(ind-1)/2];
        pHeap->store[(ind-1)/2] = temp;
        ind = (ind-1)/2;       
    }    
    return 0;
}

int findHeap(HeapType *pHeap, int key){
    int inLs = 0;
    int i=0;

    for (i=0;i<pHeap->end;i++){
        if (pHeap->store[i] == key)
            inLs = 1;
    }
    return inLs;
}

int delHeap(HeapType *pHeap, int key){
    int ind = 0;
    int temp = 0;
    if (pHeap == NULL){
        return -1;
    }
    pHeap->store[0] = pHeap->store[pHeap->end-1];
    
    while (pHeap->store[ind] < pHeap->store[(2*ind)+1] || pHeap->store[ind] < pHeap->store[(2*ind)+2]){
        if (pHeap->store[ind] < pHeap->store[(2*ind)+1]){
            temp = pHeap->store[ind];
            pHeap->store[ind] = pHeap->store[(2*ind)+1];
            pHeap->store[(2*ind)+1] = temp;
            ind = (2*ind)+1;       
        } else {
            temp = pHeap->store[ind];
            pHeap->store[ind] = pHeap->store[(2*ind)+2];
            pHeap->store[(2*ind)+2] = temp;
            ind = (2*ind)+2;       
        }
        
    }
    return 0;
}



//for stack
void push(Stack *s, int val){
    s->st[s->end] = val;
    s->end = s->end + 1;
}

int pop(Stack *s){
    int temp = s->st[s->end-1];
    s->end = s->end-1;
    return temp;
}
