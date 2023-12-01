#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def quantidadeDigitos(numero):
    quantidade = (len(str(numero)))
    print(f"A quantidade de dígitos do {numero} é igual a {quantidade}")

numero = int(input("Digite um número inteiro: "))
quantidadeDigitos(numero)