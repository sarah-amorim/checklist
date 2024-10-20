from usuarios.cadastrar_usuarios import cadastrar_usuarios
from autenticar.login import login
from limpar_tela.limpar_tela import limpar_tela
from checklist.checklist_main import *

usuarios = []

while True:
    print("\nCHECK-LIST DE TAREFAS")
    print("1 - CRIAR CONTA")
    print("2 - LOGIN")

    try:
        opcao = int(input("Escolha a ação que deseja executar: "))
    except ValueError:
        print("Digite uma opção válida!\n")
        opcao = int(input("Escolha a ação que deseja executar: "))
        break

    if opcao == 1:
        cadastrar_usuarios(users=usuarios)
        print("Usuário cadastrado com sucesso!\n")
        limpar_tela()

    elif opcao == 2:
        if not usuarios:
            print("Para fazer login é necessário cadastrar um usuário!\n")
            cadastrar_usuarios(users=usuarios)
            limpar_tela()
        else:
            login(users=usuarios)
            limpar_tela()
            checklist(users=usuarios)
