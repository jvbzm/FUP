#include <stdio.h>

int main(){
    int a,b,c;
    scanf("%d%d%d",&a,&b,&c);
    if((a<b+c) && (b<a+c) && (c<a+b)){
        if ((a==b) && (b==c)){
        printf("triangulo equilatero");
        }
        else{
            if((a==b) || (b==c) || (a==c)){
            printf("Triangulo isosceles");
            }
            else{
                printf("triangulo escaleno");
            }
        }
        }
        else{
            printf("estes valores não formam um triangulo");
        }
    return 0;
}
