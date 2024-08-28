int main(){
    int A,B;
    scanf("%d %d", &A ,&B);
    if (1<=A && B<=10000 && B>0 ){
        printf("%d\n",A+B);
        printf("%d\n",A-B);
        printf("%d\n",A*B);
        printf("%d\n",A/B);
        printf("%d\n",A%B);
    }
}