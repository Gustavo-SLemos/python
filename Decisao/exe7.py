#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))

def maior():
    if num1 > num2 and num1 > num3:
        return print(f"O maior número digitado é {num1}.")
    elif num2 > num1 and num2 > num3:
        return print(f"O maior número digitado é {num2}.")
    elif num3 > num1 and num3 > num2:
        return print(f"O maior número digitado é {num3}.")
    else:
        return print("Todos os números digitados são iguais.")
    
    

def menor():
    if num1 < num2 and num1 < num3:
        return print(f"O menor número digitado é {num1}.")
    elif num2 < num1 and num2 < num3:
        return print(f"O menor número digitado é {num2}.")
    elif num3 < num1 and num3 < num2:
        return print(f"O menor número digitado é {num3}.")


menor()
maior()