#include <stdio.h>

float G1, G2, media;
int main(){
    printf("Digita a nota da G1: ");
    scanf ("%f", &G1);
    printf("Digita a nota da G2: ");
    scanf ("%f", &G2);
    media = (G1 + G2) / 2;
    if (media >= 7){
        printf ("Aluno aprovado com media %.2f", media);
    }
    else {
            printf ("Aluno reprovado com media %.2f", media);
    }
}
    
    // .2f para pegar 2 digitos dps da virgula