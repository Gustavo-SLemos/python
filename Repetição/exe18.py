#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

conjunto = []
num1 = int(input("Digite o valor inicial do conjunto: "))
num2 = int(input("Digite o valor final do conjunto: ")) + 1

for i in range(num1, num2):
    conjunto.append(i)

menor_valor = min(conjunto)
maior_valor = max(conjunto)
soma = sum(conjunto)

print(f"O menor valor do conjunto de números é {menor_valor}")
print(f"O maior valor do conjunto de números é {maior_valor}")
print(f"A soma do conjunto de números é {soma}")