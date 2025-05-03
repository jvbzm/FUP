#include <stdio.h>
int main(){
    int capacidade,qb,qg,qm,min,soma;
    scanf("%d %d %d %d",&capacidade,&qb,&qg,&qm);
    soma = qb + qg + qm;
    min = soma/capacidade;
    if(soma%capacidade!=0){
        min = min  +1;
    }
      printf("%d",min);
}