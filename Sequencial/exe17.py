#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

area = float(input("Digite a área em metros quadrados que será pintada: "))
cobertura = area / 6
lata = 18
valor_lata = 80
galao = 3.6
valor_galao = 25

quantidade_de_latas = math.ceil(cobertura / lata)
quantidade_de_latas2 = (cobertura / lata)
preco_latas = quantidade_de_latas * valor_lata

quantidade_galao = math.ceil(cobertura/ galao)
preco_galao = quantidade_galao * valor_galao


# Cálculo para a mistura de latas e galões
quantidade_latas_mistura = math.floor(quantidade_de_latas2)
quantidade_galoes_mistura = math.ceil((cobertura - quantidade_latas_mistura * lata) / galao)
preco_total_mistura = (quantidade_latas_mistura * valor_lata) + (quantidade_galoes_mistura * valor_galao)


print(f"Quantidade de tinta necessária: {cobertura:.2f} litros")
print(f"Situação 1: Comprar apenas latas de 18 litros")
print(f"  Quantidade de latas: {quantidade_de_latas}")
print(f"  Preço total: R$ {preco_latas:.2f}")
print(f"Situação 2: Comprar apenas galões de 3,6 litros")
print(f"  Quantidade de galões: {quantidade_galao}")
print(f"  Preço total: R$ {preco_galao:.2f}")
print(f"Situação 3: Misturar latas e galões")
print(f"  Quantidade de latas: {quantidade_latas_mistura}")
print(f"  Quantidade de galões: {quantidade_galoes_mistura}")
print(f"  Preço total: R$ {preco_total_mistura:.2f}")