from usuarios.cadastrar_usuarios import cadastrar_usuarios
from autenticar.login import login
from configuracoes.limpar_tela import limpar_tela
from checklist.checklist_main import *
# from checklist.CRUD import *

usuarios = []

while True:
    print("\nCHECK-LIST DE TAREFAS")
    print("1 - CRIAR CONTA")
    print("2 - LOGIN")

    try:
        opcao = int(input("Escolha a ação que deseja executar: "))
    except ValueError:
        print("Digite uma opção válida!")
        opcao = int(input("Escolha a ação que deseja executar: "))
        break

    if opcao == 1:
        cadastrar_usuarios(users=usuarios)
        print("Usuário cadastrado com sucesso!\n")
        limpar_tela()

    elif opcao == 2:
        login(users=usuarios)
        limpar_tela()
        checklist(users=usuarios)
