#include <stdio.h>
int main(){
    int o1,o2,o3,o4, omaior;
    scanf("%d %d %d %d", &o1, &o2, &o3, &o4);
    omaior = o1;
    if (o2 > omaior) {
        omaior = o2;
    }if (o3 > omaior) {
        omaior = o3;
    }if (o4 > omaior) {
        omaior = o4;
    }
    printf("%d\n", omaior);
}