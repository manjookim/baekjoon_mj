#include <stdio.h>

int main(){
    int N, arr[100],v;
    int cnt = 0;
    scanf("%d", &N);
    for(int i=0; i<N; i++){
        scanf("%d ", &arr[i]);
    }
    scanf("%d", &v);
    for(int i=0; i<N; i++){
        if(arr[i]==v)
            cnt += 1;
    }
    printf("%d", cnt);
    return 0;
}