from autenticar.validar_email import validar_email
from limpar_tela.limpar_tela import limpar_tela


def cadastrar_usuarios(users):

    nome = input("Nome: ")
    email = input("Email: ").lower()
    senha = input("Senha: ")

    while not validar_email(email):
        # print("\n")
        limpar_tela()
        print("Erro ao realizar cadastro, digite um endereço de e-mail válido!")
        print("Tente novamente!")

        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")

    user = {
            "nome": nome,
            "email": email,
            "senha": senha
    }
    users.append(user)
