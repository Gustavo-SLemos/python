#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

while True:

    nota1 = float(input("Digita a primeira nota do aluno (0 a 10): "))
    nota2 = float(input("Digite a segunda nota do aluno (0 a 10): "))

    if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10:
    
        media = (nota1 + nota2)/2

        if media >= 7 and media <10:
          print(f"Sua nota foi {media}. Você está aprovado!")
        elif media < 7:
          print(f"Sua nota foi {media}. Você foi reprovado, não desanime, poderá tentar novamente no próximo semestre.")
        else:
          print(f"Sua nota foi {media}. Parabéns, você foi aprovado com distinção!")
        break
    else:
       print("O valor digitado deve estar entre 0 e 10, tente novamente!")