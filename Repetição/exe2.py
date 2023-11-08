#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    nome_usuario = input("Digite o nome de usuário: ")
    nome_usuario = nome_usuario.upper()
    senha = input("Digite sua senha: ")
    senha = senha.upper()

    if nome_usuario != senha:
        print("Nome e senha aceitos para cadastro!")
        break
    else:
        print("A senha não pode ser igual ao nome do usuário, tente novamente!")