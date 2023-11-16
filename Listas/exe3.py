#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista = []

while True:
    for nota in range(4):
        nota = float(input("Digite a nota do aluno de 0 a 10:  "))
        if nota >= 0 and nota <= 10:
            lista.append(nota)
        else:
            print("Nota inválida e não computada!")
            break

    media = (sum(lista))/4
    media_formatada = f"{media:.2f}"
    print(f"As notas do aluno foram: {lista}")
    print(f"A média final do aluno foi: {media_formatada}")