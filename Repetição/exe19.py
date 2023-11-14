#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

conjunto = []
num1 = int(input("Digite o valor inicial do conjunto entre 0 e 1000: "))
num2 = int(input("Digite o valor final do conjunto entre 0 e 1000: "))

if num1 < 0 or num1 > 1000 or num2 < 0 or num2 > 1000:
    print(("Valor inválido, digite novamente valores entre 0 e 1000!"))
else:
    for i in range(num1, num2):
        conjunto.append(i)

    menor_valor = min(conjunto)
    maior_valor = max(conjunto) + 1
    soma = sum(conjunto)

    print(f"O menor valor do conjunto de números é {menor_valor}")
    print(f"O maior valor do conjunto de números é {maior_valor}")
    print(f"A soma do conjunto de números é {soma}")