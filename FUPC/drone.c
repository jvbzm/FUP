#include <stdio.h>
int main(){
    int A,B,C,H,L, totalabc, totalhl;
    scanf("%d %d %d %d %d",&A,&B,&C,&H,&L);
    totalabc = (A + B + C)/3;
    totalhl = (H*L)/2;
    if(A>=100){
        printf("N");
    }
    else if(B>=100){
        printf("N");
    }
    else if(C>=100){
        printf("N");
    }
    else if(H>=100){
        printf("N");
    }
    else if(L>=100){
        printf("N");
    }
    else if(totalabc<totalhl){
        printf("S");
    }
    else{
        printf("N");
    }
}