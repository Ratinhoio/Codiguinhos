#include <stdio.h>
int idade;
int main() {
    printf ("Sua idade: \n");
    scanf ("%d", &idade);
    if (idade >= 18) {
        printf ("Voce esta na Categoria Principal");
    }
    else {
        printf ("Voce esta na Categoria Infantil");
    }
}