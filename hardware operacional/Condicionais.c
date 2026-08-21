#include <stdio.h>
int main()
{
    float n1, n2, media, exame, media_final;
    printf("Digite as notas da G1 e G2: ");
    scanf("%f %f", &n1, &n2);
    media = (n1 + n2) / 2;
    if (media >= 7){
    printf ("Aluno aprovado com media: %.2f", media);
    }
    else if (media >= 3){
        printf ("Media: %0.2f\n", media);
        printf ("Digite a nota do exame: \n");
        scanf ("%f", &exame);
        media_final = (exame + media)/2;
    if (media_final >= 5){
        printf ("Aluno aprovado com media: %.2f", media_final);
    }
        else{
            printf ("Aluno reprovado com media: %.2f", media_final);
        }
    }
    else{
            printf("Aluno reprovado com media: %.2f", media);
        }
    return (0);
}