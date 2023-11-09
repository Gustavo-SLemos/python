#Faça um programa que leia 5 números e informe a soma e a média dos números.

lista = []

for i in range(5):
    i = int(input("Digite um número: "))
    lista.append(i)

soma = sum(lista)
media = sum(lista)/5

print(f"A soma dos números da lista é igual a {soma}")
print(f"A média dos números da lista é igual a {media}")