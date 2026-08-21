#include <stdio.h>
float CustoGasolina (float distancia, float KmLitro, float precoLitro) {
    return (distancia / KmLitro) * precoLitro;
}

int main() {
    float distancia, KmLitro, precoLitro, custoTotal;
    printf ("Digite o consumo do veiculo (Km por Litro): ");
    scanf("%f", &KmLitro);
    printf ("Digite a distancia percorrida na viagem (Km): ");
    scanf ("%f", &distancia);
    printf ("Digite o preço do litro da gasolina (Reais): ");
    scanf ("%f", &precoLitro);
    custoTotal = CustoGasolina (distancia, KmLitro, precoLitro);
    printf ("O custo total de gasolina para a viagem foi de: R$ %.2f", custoTotal);
    return 0;
}