#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

while True:
    turno = input("Em que turno você estuda? Responda com 'M'-matutino, 'V'-vespertino ou 'N'-noturno: ")
    turno = turno.upper()

    if turno == 'M':
        print("Bom dia!")
        break
    elif turno == 'V':
        print("Boa tarde!")
        break
    elif turno == 'N':
        print("Boa noite!")
        break
    else:
        print("Valor inválido!")