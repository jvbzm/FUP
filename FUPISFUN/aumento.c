#include <stdio.h>
int main(){
    double sal, nsal;
    scanf("%lf",&sal);
    if(sal<=1000){
        nsal = (sal * 0.20) + sal;
    }
    else if(sal<=1500){
        nsal = (sal * 0.15) + sal;
    }
    else if(sal<=2000){
        nsal = (sal * 0.10) + sal;
    }
    else if(sal>=2000){
        nsal = (sal * 0.05) + sal;
    }
    printf("%.2lf",nsal);
}