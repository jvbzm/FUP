#include <stdio.h>
int main() {
    int valor,c1,c2,prox1,prox2;
    scanf("%d%d%d",&valor,&c1,&c2);
    if (valor > c1)
        prox1 = valor-c1;
    else
        prox1 = c1-valor;
    if (valor > c2)
        prox2 = valor - c2;
    else
        prox2 = c2 - valor;
    if (prox1 < prox2) {
        printf("primeiro");
    } else if (prox2 < prox1) {
        printf("segundo");
    } else {
        printf("empate");
    }
}