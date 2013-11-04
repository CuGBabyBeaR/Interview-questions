/* 
 * CuGBabyBeaR  
 */

#include "stdio.h"

int volume_calcuate(int[],int);

int main(int argc, char const *argv[]){
    int testcase_1[9] = {2,5,1,2,3,4,7,7,6};
    int testcase_2[10] = {2,5,1,3,1,2,1,7,7,6};
    int testcase_3[9] = {6,1,4,6,7,5,1,6,4};

    printf("Case testcase_1 total volume : %i\n",volume_calcuate(testcase_1,9));
    printf("Case testcase_2 total volume : %i\n",volume_calcuate(testcase_2,10));
    printf("Case testcase_3 total volume : %i\n",volume_calcuate(testcase_3,9));
    return 0;
}

int volume_calcuate(int walls[] , int length){
    int * p_l = &walls[0];
    int * p_r = &walls[length-1];
    int max_l = walls[0];
    int max_r = walls[length-1];

    int total_volume = 0;

    while(p_r > p_l){
        if (max_l < max_r){
            p_l++;
            if (*p_l >= max_l){
                max_l = *p_l;
            }else{
                total_volume += max_l - *p_l;
            }
        }else{
            p_r--;
            if (*p_r >= max_r){
                max_r = *p_r;
            }
            else{
                total_volume += max_r - *p_r;
            }
        }
    }
    return total_volume;
}