int main(){
    int N;
    scanf("%d", &N);
    for(int i=1;i<N+1;i++){
        for(int j=N-i;j>0;j--)
            printf(" ");
        for(int k=1;k<=i;k++)
            printf("*");
        printf("\n");
    }
}