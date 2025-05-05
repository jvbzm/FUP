#include <stdio.h>
int main(){
    int ded1,ded2,total;
    char jog1,p,i;
    scanf("%c %d %d",&jog1,&ded1,&ded2);
    switch(jog1){
        case 'p':
        total = ded1 + ded2;
        if(total%2 == 0){
            printf("Venceu");
        }else{
            printf("Perdeu");
        }break;
        
        case 'i':
        total = ded1 + ded2;
        if(total%3==0){
            printf("Venceu");
        }else{
            printf("Perdeu");
        }break;
    }
}