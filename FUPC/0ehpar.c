#include <stdio.h>
int main(){
    int n1,n2,par;
    par=0;
    scanf("%d%d",&n1,&n2);
    if(n2<n1){
        printf("invalido");
        return 0;
    }
    if(n1 % 2 !=0){
        n1++;
    }
    for(int i=n1;i<=n2;i+=2){
        par+=i;
    }
    printf("%d",par);
    
}