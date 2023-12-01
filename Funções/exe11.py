#Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

from datetime import datetime

def dataPorExtenso(data):
    try:
        data_ajustada = datetime.strptime(data, '%d-%m-%Y')
        data_formatada = data_ajustada.strftime('d% de %B de %Y')

        return data_formatada
    
    except ValueError:
        return None

data_input = input("Digite uma data no formato DD/MM/AAAA: ")
data_formatada = dataPorExtenso(data_input)

if data_formatada:
    print(f"A data por extenso é: {data_formatada}")
else:
    print("Data inválida. Digite no formato correto.")