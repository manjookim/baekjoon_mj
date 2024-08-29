int main(){
    int X,N,a,b,price=0;
    scanf("%d", &X);
    scanf("%d", &N);
    for(int i=0;i<N;i++){
        scanf("%d %d", &a, &b);
        price += a*b;
    }
    if (X == price) printf("Yes");
    else printf("No");
}