#include <stdio.h>
#include <math.h>
int main() {
    float a, b, c, delta, x1, x2;
    scanf("%f %f %f", &a, &b, &c);
    if (a == 0) {
        x1 = 0;
        x2 = 0;
        printf("%.2f\n", x1);
        return 0;
    }
    delta = b * b - 4 * a * c;
    if (delta < 0) {
        printf("nao ha raiz real\n");
    } else {
        x1 = (-b + sqrt(delta)) / (2 * a);
        x2 = (-b - sqrt(delta)) / (2 * a);
        if (x1 == x2) {
            printf("%.2f\n", x1);
        } else {
            printf("%.2f %.2f", x1, x2);
        }
    }
    return 0;
}