#include <stdio.h>
#include <string.h>

int main(){
    int n, sum;
    char test[80];
    scanf("%d", &n);

    for(int i=0; i<n;i++){
        sum = 0;
        int cnt = 0;
        scanf("%s", test);
        for(int j=0; j<strlen(test); j++){
            if(test[j] == 'O'){
                cnt ++;
                sum += cnt;  
                //printf("sum :", "%d", sum);
            }
            else cnt = 0;
        }
        printf("%d\n", sum); 
    }

    return 0;
}