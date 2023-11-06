#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
cobertura = area / 3
lata = 18
valor = 80

quantidade_de_latas = math.ceil(cobertura / lata)
preco_total = quantidade_de_latas * valor

print(f"A quantidade de latas necessárias para a pintura é {quantidade_de_latas} e o valor total da compra é de R${preco_total}.")