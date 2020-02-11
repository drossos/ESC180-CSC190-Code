/* container to store data that is input with an
 * unknown number of items.
 *  *
 *   * Note how we get the data:
 *    * -while loop (because the number of iterations is unknown)
 *     * -scanf returns EOF, or End-Of-File, when "nothing" has been input
 *      * -for each iteration, we stuff the input data into a linked list
 *       *
 *        * Usage:
 *         * gcc getData.c
 *          * echo "1 2 3 4 5 6 7 8     9      10" | ./a.out
 *           * should report 10 items read and dump it out
 *            * -> white space is ignored (space, tab, return)
 *             *
 *              * Assignment:
 *               * -modify this code so that it handles input "char" data
 *                *  rather than ints (trivial modification)
 *                 * echo "abcdef" | ./a.out
 *                  * should report 7 items read
 *                   * (white space is representable by the char hence the
 *                    * final return you enter is stored as a char)
 *                     */

#include <stdio.h>
#include <stdlib.h>

struct llnode {
   char value;
   struct llnode *next;
};
typedef struct llnode llnode;


int llnode_add_to_tail(llnode **x,char value) {
   if (x==NULL) { return -1; }
   if (*x==NULL) {
      *x = (llnode *) malloc(sizeof(llnode));
      (*x)->value = value;
      (*x)->next = NULL;
      return 0;
   } else {
      return llnode_add_to_tail(&((*x)->next),value);
   }
}

int llnode_print_from_head(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      printf("%c\n",x->value);
      return llnode_print_from_head(x->next);
   }
}

int llnode_print_from_tail(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      if (x->next == NULL) {
         printf("%c\n",x->value);
     return 0;
      } else {
         llnode_print_from_tail(x->next);
         printf("%c\n",x->value);
     return 0;
      }
   }
}

int llnode_add_to_head(llnode **x , char value){
    llnode *temp = NULL;
    if (x==NULL){
       return -1;
   }
   if (*x==NULL) {
      *x = (llnode *) malloc(sizeof(llnode));
      (*x)->value = value;
      (*x)->next = NULL;
      return 0;
   } else {
       temp = *x;
       *x = (llnode *) malloc (sizeof(llnode));
       (*x)->value = value;
       (*x)->next = temp;
        return 0;   
   }
}

int push(llnode **x, char value){
    return llnode_add_to_tail(x,value);
}

int pop(llnode **x, char *return_value){
    if (x == NULL || *x == NULL){
        return_value = '\0';
        return -1;
    }
    
    //case only one element in stack
    if ((*x)->next == NULL){
        *return_value = (*x)->value;
        *x = NULL;
        return 0;   
    }
    if ( ((*x)->next)->next == NULL){
        *return_value = ((*x)->next)->value;
        (*x)->next = NULL;
        return 0;
    }
    return pop(&((*x)->next), return_value);
}

int isEmpty(llnode **x){
    if (*x == NULL){
        return 0;
    } else {
        return -1;
    }
}   

int main(void) {
   int n=0;
   char popVal='\0';
   char value='\0';
   char rvalue='\0';
   int failInd=0;
   llnode *input_list=NULL;

   while (scanf("%c",&value) != EOF) {
      n=n+1;
      //printf("%c",value);
      if(value == '[' || value == '(' || value == '{'){
        //printf("%d \n",value);
        push(&input_list,value);
      }
      
      //printf("%c",value);
      if(value == ']' || value == ')' || value == '}'){
         //printf("poping");
         pop(&input_list,&popVal);
        //printf("%c",popVal);

        //printf("%c",value);
        if (popVal == '\0' || popVal == '[' && value != ']' || popVal == '(' && value != ')' || popVal == '{' && value != '}'){
            printf("FAIL,%d",failInd);
            return 0;
        }  
      }
      failInd++;
   }
   
   if (isEmpty(&input_list) == 0){
       printf("PASS");
   }else{
       printf("FAIL,%d",failInd);
   }

   //printf("INFO: you entered %d items\n",n);
   //rvalue=llnode_print_from_tail(input_list);
   //if ( !(rvalue==0) ) { printf("ERR: llnode_print returned an error\n"); }
   //pop(&input_list, &value); 
   //printf("pop value %c", value);
   return 0;
}

