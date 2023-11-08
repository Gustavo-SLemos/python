#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';


def validar_nome(nome):
    return len(nome) > 3

def validar_idade(idade):
    return 0 <= idade <= 150

def validar_salario(salario):
    return salario > 0

def validar_sexo(sexo):
    return sexo in ['f', 'm']

def validar_estado_civil(estado_civil):
    return estado_civil in ['s', 'c', 'v', 'd']


def main():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    salario = float(input("Digite seu salário: "))
    sexo = input("Informe seu sexo (f ou m): ").lower()
    estado_civil = input("Informe seu estado civil (s/c/v/d): ").lower()

    if validar_nome(nome):
        print("Nome válido")
    else:
        print("O nome deve ter pelo menos 3 caracteres. Tente novamente!")

    if validar_idade(idade):
        print("idade válida")
    else:
        print("A idade deve estar entre 0 e 150. Tente novamente!")
    
    if validar_salario(salario):
        print("salário válido")
    else:
        print("O salário deve ser maior que 0. Tente novamente!")

    if validar_sexo(sexo):
        print("Sexo válido")
    else:
        print("O sexo deve ser f ou m. Tente novamente!")

    if validar_estado_civil(estado_civil):
        print("Estado civil válido")
    else:
        print("O estado civil deve ser s, c, v ou d. Tente novamente!")

main()