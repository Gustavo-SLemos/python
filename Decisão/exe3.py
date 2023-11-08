#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

while True:
    
    sexo = input("Informe seu sexo com F para feminino ou M para masculino: ")
    sexo1 = sexo.upper()

    if sexo1 == "F":
        print("Sexo: Feminino")
        break
    elif sexo1 == "M":
        print("Sexo: Masculino")
        break
    else:
        print("Sexo inválido, tente novamente!")