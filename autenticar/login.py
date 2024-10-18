from autenticar.validar_email import validar_email
from limpar_tela.limpar_tela import limpar_tela


def login(users):
    email = input("Email: ").lower()
    validar_email(email)
    senha = input("Senha: ")

    while not validar_email(email):
        limpar_tela()
        print("Erro ao realizar login, digite um endereço de e-mail válido!")
        email = input("Email: ").lower()
        senha = input("Senha: ")

    for user in users:
        if user["email"] == email and user["senha"] == senha:
            print("Usuário encontrado")
        else:
            limpar_tela()
            print("Usuário não encontrado, tente novamente!\n")
            return login(users)
