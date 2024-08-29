#include <math.h>

int main(){
    long long A,B,C;
    scanf("%lld %lld %lld", &A,&B,&C);
    if (1<=A && A<=pow(10,12) && 1<=B && B<=pow(10,12) && 1<=C && C<=pow(10,12)){
        printf("%lld", A+B+C);
    }
}