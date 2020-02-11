#include <stdio.h>
/*I know this code doesn't work and is just a step above pseudo code, but I keep falling alseep at my desk and p. sure my eyes are bleeding*/
 
  int ge_fw(float *matrix, int rows, int cols, float *matrix_out);
  int ge_bw(float *matrix, int rows, int cols, float *matrix_out);

  int ge_fw(float *matrix, int rows, int cols, float *matrix_out){
    //matrix = mat
    //overallMatrix = mat
    int rowCount  = 0;
    int i = 0;
    int j = 0;
    float* temp = NULL;
    float factor = 0;
    int countR = 0;
    int countC = 0;
    int tempRows = rows;
    int tempCols = cols; /*allocating memroy*/
   *matrix_out = (float**)malloc(rows*sizeof(float*));
    for (i=0;i<rows;i++){
        matrix_out[i] = (float*)malloc(cols*sizeof(float));
    }

    while(1 == 0){
        for (i=0;rows;i++){
            if (matrix[i* + 0] != 0 && matrix[0][0] == 0){
                temp = matrix[0];
                matrix[0] = list(matrix[i]);
                matrix[i] = temp;
                *matrix_out[rowCount] = (float*) malloc((rowCount+cols)*sizeof(float));

                *matrix_out[rowCount][rowCount] =matrix[0];
                rowCount += 1;
                break;
            }
        }
        for (i=1;i<rows,i++){
            if (matrix[i][0] != 0){
                factor = matrix[i][0] / matrix[0][0];
                for (j=0;j<cols;j++){
                    matrix[i][j] = matrix[i][j] + -1 * factor * matrix[0][j]
                }    
            }
        }
        *temp = (float**)malloc((rows-1)*sizeof(float*));
        for (i=0;i<rows;i++){
            temp[i] = (float*)malloc((cols-1)*sizeof(float));
        }
        
        countR = 0;
        for (i=1;i<rows;i++){
            countC = 0;
            for (j=1;<cols;j++){
                temp[countR][countC] = matrix[i][j];
                countC += 1;
            }
            countR += 1;
        //print(overallMatrix)
        }
        if tempRows <= 1 || tempCols <= 1{
            break;
        }
        else{
            tempRows--;
            tempCols--;
            matrix = temp;
        }
    }
    return 0;
  }

 
int ge_bw(float *matrix, int rows, int cols, float *matrix_out){
    int rowCount = rows -1;
    int i =0 ;
    int j=0;
    int ind;
    float fact;
    float multFact;
    int countC = 0;
    int countR = 0;
    float* temp = NULL;

    *matrix_out = (float**)malloc(rows*sizeof(float*));
    for (i=0;i<rows;i++){
        matrix_out[i] = (float*)malloc(cols*sizeof(float));
    }

    while(1 == 1){
        ind = 0
        for (i=0;i<cols-1;i++){
            if matrix[rows-1][i] != 0{
                fact = i;
                break;
            }
            ind += 1;
        }
        if (ind >= cols){
            ind =0;
        }
        for (i=1;i<cols;i++){
            if(matrix[rows-1][i] == 1){
                break;
            }
            else{
                matrix[rows-1][i] = matrix[rows-1]][i] / fact;
            }
        }
        matrix_out[rowCount] =matrix[rowCount];
        rowCount -= 1;

        
        for (i=1;i<rows-1;i++){
          
            multFact = matrix[i][ind];
            for (j=1;cols;j++){
                
                matrix[i][j] = matrix[i][j]+ -1* matrix[rows-1][j]*multFact;
               
            }
        }
        
        *temp = (float**)malloc((rows-1)*sizeof(float*));
        for (i=0;i<rows;i++){
            temp[i] = (float*)malloc((cols-1)*sizeof(float));
        }

        countR = 0;
        
        for (i=1;i<rows-1;i++){
            countC = 0;

            for (j=0;j<cols;j++){
                temp[countR][countC] = matrix[i][j];
                countC += 1;
            }
            
            countR += 1;
        }
        if rowCount < 0 or rows <= 0 or cols <= 0{
           
            break;
        }
        else{
            matrix = temp;
        }
           
    }

    return 0;
}
