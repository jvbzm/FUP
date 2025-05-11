#include <stdio.h>
int main(){
    int e1,e2,e3,meio;
    scanf("%d%d%d",&e1,&e2,&e3);
    if((e1 > e2 && e1 < e3) || (e1 > e3 && e1 < e2)){
        printf("%d",e1);
    }else if((e2 > e1 && e2 < e3) || (e2 > e3 && e2 < e1)){
        printf("%d",e2);
    }else if((e3 > e1 && e3 < e2) || (e3 > e2 && e3 < e1)){
        printf("%d",e3);
    }
}