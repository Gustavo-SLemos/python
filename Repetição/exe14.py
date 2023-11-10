#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

pares = 0
impares = 0

for i in range(10):
    numeros = int(input(f"Digite o {i + 1} número: "))


    if numeros %2 == 0:
        pares += 1
    else:
        impares += 1

print(f"A quantidade de números pares é {pares}.")
print(f"A quantidade de números impares é {impares}.")