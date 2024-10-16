from autenticar.validar_email import validar_email


def login(users):
    email = input("Email: ").lower()
    validar_email(email)
    senha = input("Senha: ")

    while not validar_email(email):
        print("Erro ao realizar login, digite um endereço de e-mail válido!")
        print("\n")
        email = input("Email: ").lower()
        senha = input("Senha: ")

    for user in users:
        if user["email"] == email and user["senha"] == senha:
            nome = user["nome"]
            print(f"Olá, {nome}!\n")
            # break
        else:
            print("Usuário não encontrado!")
            break
