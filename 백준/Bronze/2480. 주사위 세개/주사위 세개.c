int max3(int a,int b,int c){
    int max = a;
    if (b>max) max=b;
    if (c>max) max=c;
    return max;
}

int main(){
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    if (a==b || b==c || a==c){
        if (a==b && b==c) printf("%d",10000+a*1000);
        else {
            if (a==b || b==c) printf("%d",1000+b*100);  
            else printf("%d",1000+c*100);
        }
    }
    else 
        printf("%d",max3(a,b,c)*100);
}
