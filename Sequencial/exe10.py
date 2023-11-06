#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# C = 5 * ((F-32) / 9)

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = round(((celsius * 9/5) + 32), 2)

print(f"A temperatura em fahrenheit é {fahrenheit}F")