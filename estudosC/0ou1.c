#include <stdio.h>
int main(){
    int jog1,jog2,jog3,jogt;
    scanf("%d %d %d",&jog1,&jog2,&jog3);
    jogt = jog1 +jog2+jog3;
    if(jogt%3==0){
        printf("empate");
    }else if(jog1!=jog2 && jog1!=jog3){
        printf("jog1");
    }else if(jog2!=jog1 && jog2!=jog3){
        printf("jog2");
    }else if(jog3!=jog2 && jog3!=jog1){
        printf("jog3");
    }
}