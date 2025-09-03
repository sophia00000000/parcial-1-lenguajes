#include <stdio.h>
#include <time.h>

// Función recursiva factorial
long long factorial(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}

int main() {
    int valores[] = {50, 100, 150, 200};
    int n = sizeof(valores) / sizeof(valores[0]);
    double tiempos[n];

    for (int i = 0; i < n; i++) {
        clock_t inicio = clock();
        long long resultado = factorial(valores[i]);
        clock_t fin = clock();

        tiempos[i] = (double)(fin - inicio) / CLOCKS_PER_SEC;
    }

    printf("\nTiempos");
    for (int i = 0; i < n; i++) {
        printf("%f", tiempos[i]);
        if (i < n - 1) printf(", ");
    }
    printf("\n");

    return 0;
}
