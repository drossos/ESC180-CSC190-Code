
int main(void){

}    
 
struct stack{
    int *arr;
    int end;   
}

int pop(struct stack *s){
    return (s->arr)[(s->end)];
} 

int push(struct stack *s, int val){
    (s->end) = (s->end) + 1;
    (s->arr)[(s->end)] = val;
    return 0;
}

