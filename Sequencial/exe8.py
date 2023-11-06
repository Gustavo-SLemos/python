#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_por_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite quantas horas você trabalha por mês: "))

salario = round((ganho_por_hora * horas_trabalhadas), 2)

print(f"O seu salário no mês é de R${salario}")