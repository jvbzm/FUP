#include <stdio.h>

int main() {
    int op;
    scanf("%d",&op);
        switch(op){
    case 1:
        printf("voce escolheu 1");
        break;
    case 2:
        printf("voce escolheu 2");
        break;
    case 3:
        printf("voce escolheu 3");
        break;
    default:
        printf("opcao invalida");
    }
    return 0;
}
