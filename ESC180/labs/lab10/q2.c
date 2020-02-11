#include <stdio.h>

struct blah {
    int id;
    int val[4];
    char label[4];
    int *data;
};

int main(void){
    struct blah temp;
    printf("%d",sizeof(temp));
}
