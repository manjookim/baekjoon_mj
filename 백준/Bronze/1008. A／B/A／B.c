int main(){
    int A,B;
    scanf("%d", &A), scanf("%d",&B);
    if (0<A && B<10){
        printf("%.9f", (double)A/B);
    }
}