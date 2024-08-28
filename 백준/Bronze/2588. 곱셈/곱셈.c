int main(){
    int A,B;
    scanf("%d %d",&A, &B);
    printf("%d\n", A*(B%10));
    printf("%d\n", A*((B%100)/10));
    printf("%d\n", A*(B/100));
    printf("%d", (A*(B%10))+(A*((B%100)/10)*10)+(A*(B/100)*100));

}