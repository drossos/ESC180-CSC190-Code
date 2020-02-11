
int anlboard(int *T, int sizeT){
    int i;
    int k;
    if (sizeT != 9){
        return -1;
    }
    
        
    for(i=0;i<sizeT;i++){
        if(T[i] != 1 && T[i] != 2 && T[i] != 0){
            return -1;
        }
    }

    for (i =0 ; i < 3; i++){
        if ( T[i] == T[i+3] && T[i+3] == T[i+6]){
            if(T[i] == 1){
                return 1;
            }
            else if (T[i] == 2){
                return 2;
            }
        } else if(T[i*3] == T[i*3 + 1] && T[i*3] == T[i*3+2]){
            if(T[i*3] == 1){
                return 1;
                }
            else if(T[i*3] == 2){
                return 2;
                }
            }
    }

    if (T[0] == T[4] && T[0] == T[8] || T[2] == T[4] && T[2] == T[6]){
        if (T[4] == 1){
            return 1;
        }
        else if (T[4] == 2){
        return 2;
        }
    }

    for (k = 0; k < sizeT; k++){
        if (T[k] == 0){
        return 0;
        }
    }

    return 3;
}

