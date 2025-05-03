#include <stdio.h>
int main(){
    int n1,n2, ma,mfinal;
    scanf("%d %d", &n1,&n2);
    ma = (n1+n2)/2;
    if(ma>=7){
        printf("aprovado");
    }
    else if(ma<4){
        printf("reprovado");
    }
    else if(ma==4 || ma<7){
        scanf("%d",&mfinal);
        mfinal = (ma + mfinal)/2;
            if(mfinal>=5){
                printf("aprovado na final");
            }
            else{
                printf("reprovado na final");
            }
    }
}