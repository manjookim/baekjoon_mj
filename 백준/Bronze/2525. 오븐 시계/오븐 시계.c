int main(){
    int A,B,C,D,E;
    scanf("%d %d", &A, &B);
    scanf("%d", &C);
    D = A+C/60;
    E = B+C%60;
    if (E>=60){
        E -= 60, D += 1;
        if (D>23)
            printf("%d %d", D-24, E);
        else
            printf("%d %d", D, E);
    }
    else{
        if (D>23)
            printf("%d %d", D-24, E);
        else
            printf("%d %d", D, E);
    }
        
    
}