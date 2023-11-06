#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

while True:

    letra = input("Digite uma letra: ")
    letra = letra.upper()


    if len(letra) == 1 and letra.isalpha():
        if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
          print("A letra digitada é uma vogal!")
          break
        else:
          print("A letra digitada é uma consoante!")
          break

    else:
       print("O caractere digitado não é letra ou tem mais de uma letra, tente novamente!")