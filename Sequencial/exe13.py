#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

sexo = input("Digite seu sexo: M para masculino e F para feminino: ")
sexo_ok = sexo.upper()
altura = float(input("Digite a sua altura: "))
peso_ideal_h = round(((72.7 * altura) - 58), 2)
peso_ideal_m = round(((62.1 * altura) - 44.7), 2)

if sexo_ok == "M":
    print(f"Seu peso ideal é {peso_ideal_h}kg")
elif sexo_ok == "F":
    print(f"Seu peso ideal é {peso_ideal_m} kg")
else:
    print("Opção inexistente, tente outra vez")