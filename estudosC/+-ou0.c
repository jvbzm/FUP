#include <stdio.h>
int main(){
    int n1;
    scanf("%d",&n1);
    if(n1==0){
        printf("nulo");
    }else if(n1>0){
        printf("positivo");
    }else{
        printf("negativo");
    }
}