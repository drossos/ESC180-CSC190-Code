#include <stdio.h>

unsigned char FSR(unsigned char x){
    unsigned char oldbit0 = x & 0x1; /* extract bit 0 */
    unsigned char r = x >> 1;        /* shift right   */
    unsigned char newbit7 = oldbit0 << 7; /* move bit0 to the bit7 pos */
    r = r | newbit7; /* rotate the old value of bit 0 into the bit 7 pos */
    return r;
}

unsigned char prng(unsigned char x, unsigned char pattern){
    unsigned char temp = FSR(x);
    return temp ^ pattern;
}

int crypt(char *data, unsigned int size, unsigned char password){
    unsigned char prngVal = password;
    int i = 0;
    
    if (data == NULL || password == 0){
        return -1;
    }

    for (i=0;i<size;i++){
        prngVal = prng(prngVal,0xb8);
        data[i] = data[i] ^ prngVal;
    }
    return 0;
}
/*
int main(void){
    unsigned char x = 0x7;
    unsigned char temp = FSR(x);
    
    printf("%x\n",0x7);
    printf("%x",prng(x,0xb8));
}
*/

