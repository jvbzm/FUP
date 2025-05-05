#include <stdio.h>
int main(){
    char ct2;
    float c1, valor;
    scanf("%f %c %f",&c1,&ct2,&valor);
    switch(ct2){
        case 'm':
        if(c1>valor){
            printf("segundo");
        }else{
            printf("primeiro");
        }break;
        case 'M':
        if(c1<valor){
            printf("segundo");
        }else{
            printf("primeiro");
        }break;
    }
}
    