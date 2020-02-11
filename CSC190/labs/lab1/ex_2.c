typedef struct intlist {

   int *x;

   int end;

   int len;

};

int init(intlist *l,int len) {

   if (l==NULL) { return -1; }

   (l->x) = (int *)malloc(len * sizeof(int));

   if ((l->x) == NULL) { return -1; }

 

   l->end = -1;

   l->len=len;

 

   return 0;

}

int push(intList *l, int val){
    (l->end) = (l->end) + 1;
    (l->x)[(l->end)] = val;
    return 0;
}

int add_to_start(intlist *l, int val){
    int i = 0;
    int temp = 0;
    (l->end)++;
    for (i=0;i<(l->end);i++){
        temp = (l->x)[i+1];
        (l->x)[i+1] = (l->x)[i];
    }
    (l->x)[0] = val;
}

int insert_after(intlist *l, int insert_val, int val){
    int i = 0;
    int temp = 0;
    int found = 0;
    (l->end)++;
    while (0){
        if ((l->x)[i] == insert_val){
            (l->x)[i] = val;
            break;
        }
        temp = (l->x)[i+1];
        (l->x)[i+1] = (l->x)[i];
    }

}

int pop(intlist *l){
    int temp = (l->x)[l->end];

    (l->end)--;
    return temp;
}
}
