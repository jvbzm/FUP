#include <stdio.h>
int main() {
    int n;
    double form = 0;
    for (int i = 1; i <= 33; i++) {
        scanf("%d", &n);

        if (i % 2 == 0) {
            form += (double)n / (i + 2);
        } 
        else{
            form += (double)n / (i + 3);
        }
    }
    printf("%.2lf", form);
    return 0;
}