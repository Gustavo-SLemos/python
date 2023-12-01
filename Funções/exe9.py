#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(numero):
    numero_str = str(numero)
    numero_reverso = numero_str[::-1]
    return numero_reverso

numero = int(input("Digite um número: "))
resultado = reverso(numero)
print(f"O número reverso de {numero} é {resultado}")