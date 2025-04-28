#include <stdio.h>

int main() {
    float n1,n2,opf;
    char op;
    scanf("%c %f %f",&op,&n1,&n2);
        switch(op){
    case '+':
        opf = n1+n2;
        printf("%f",opf);
        break;
    case '-':
        opf = n1-n2;
        printf("%f",opf);
        break;
    case '*':
        opf = n1*n2;
        printf("%f",opf);
        break;
    case '/':
        opf = n1/n2;
        printf("%f",opf);
        break;
    default:
        printf("operacao invalida");
        }
    }