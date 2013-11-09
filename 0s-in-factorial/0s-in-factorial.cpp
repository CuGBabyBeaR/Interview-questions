#include<stdio.h>

int getZeros(int);

int main(int argc, char const *argv[]){
    int testcases[] = {100,1000,5000};
    int results[] = {24,249,1249};

    for (int i = 0; i < 3; ++i){
        int num = getZeros(testcases[i]);
        if (num == results[i]){
            printf("Currect. In the end of %d!, there are %d 0s.\n",testcases[i] ,num);
        }else{
            printf("Incurrect. In the end of %d!, there should be %d 0s , result is %d.",testcases[i],results[i],num);
        }
    }
    return 0;
}

int getZeros(int n){
    int res = 0;
    int d = 5;
    while(d <= n) {
        res += n/d;
        d *= 5;
    }
    return res;
}
