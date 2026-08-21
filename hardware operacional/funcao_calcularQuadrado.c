#include <stdio.h>
int CalcularQuadrado (int n){
    return n*n;
}

int main () {
    int numero, resultado;
    printf ("Digite um numero inteiro:");
    scanf ("%d", &numero);
    resultado = CalcularQuadrado (numero);
    printf ("O valor quadrado eh %d", resultado);
    return 0;
}