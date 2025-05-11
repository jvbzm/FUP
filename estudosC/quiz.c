#include <stdio.h>
int main() {
    int resposta;
    char q1, q2, q3, q4;
    resposta = 0;
    scanf("%c %c %c %c", &q1,&q2,&q3,&q4);
    if (q1 == 'd') resposta++;
    if (q2 == 'a') resposta++;
    if (q3 == 'c') resposta++;
    if (q4 == 'd') resposta++;
    if (resposta == 0) {
        printf("Nunca assistiu\n");
    } else if (resposta == 1) {
        printf("Ja ouviu falar\n");
    } else if (resposta == 2) {
        printf("Interessado no assunto\n");
    } else if (resposta == 3) {
        printf("Fa\n");
    } else {
        printf("Super fa\n");
    }
}