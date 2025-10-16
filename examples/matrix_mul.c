#include <stdio.h>

void multiply(const int a[2][2], const int b[2][2], int result[2][2]) {
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
            result[i][j] = 0;
            for (int k = 0; k < 2; ++k) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}

int main(void) {
    int a[2][2] = {{1, 2}, {3, 4}};
    int b[2][2] = {{5, 6}, {7, 8}};
    int result[2][2];
    multiply(a, b, result);
    printf("Result matrix:\n");
    for (int i = 0; i < 2; ++i) {
        printf("%d %d\n", result[i][0], result[i][1]);
    }
    return 0;
}
