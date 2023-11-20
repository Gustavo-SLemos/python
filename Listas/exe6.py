#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

notas = []
alunos = []

for aluno in range(10):
    for i in range(4):
        nota = float(input("Digite a nota do aluno: "))
        notas.append(nota)

        if nota >= 7:
            print(notas)