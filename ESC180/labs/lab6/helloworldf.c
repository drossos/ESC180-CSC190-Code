#include <stdio.h>

float bsqrt(float x, float tol);
float abs(float x ,float y);

float bsqrt(float x, float tol){
    float guess = x/2;
    while (abs(x, (guess * guess)) > tol){
        guess = (guess + (x/guess))/2;
    }
    return guess;
}

float abs(float x, float y){
    if (x-y < 0)
        return -1 * (x-y);
    return x-y;
}

int main(void){
    int i = 0;
    for (i = 0; i < 10; i++){
    printf("The sqrt of %d is %f\n",i,bsqrt(i,.1));
    }   


}
