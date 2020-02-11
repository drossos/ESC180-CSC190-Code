int anlboard(char *T, int sizeT){
    int i;
    int k;
    if (sizeT != 9){
        return -1;
    }
    for(i=0;i<sizeT;i++){
        if(T[i] != 'O' && T[i] != 'X' && T[i] != '-'){
            return -1;
        }
    }
    for (i =0 ; i < 3; i++){
        if ( T[i] == T[i+3] && T[i+3] == T[i+6]){
            if(T[i] == 'X'){
                return 1;
            }
            else if (T[i] == 'O'){
                return 2;
            }
        } else if(T[i*3] == T[i*3 + 1] && T[i*3] == T[i*3+2]){
            if(T[i*3] == 'X'){
                return 1;
                }
            else if(T[i*3] == 'O'){
                return 2;
                }
            }
    }

    if (T[0] == T[4] && T[0] == T[8] || T[2] == T[4] && T[2] == T[6]){
        if (T[4] == 'X'){
            return 1;
        }
        else if (T[4] == 'O'){
        return 2;
        }
    }

    

    for (k = 0; k < sizeT; k++){
        if (T[k] == '-'){
        return 0;
        }
    }


    return 3;
}

