from checklist.CRUD.funcionalidades import *

atividades = []


def checklist(users):
    for user in users:
        nome = user["nome"]
        print(f"Olá, {nome}!\n")
        break

    while True:
        print("1 - CRIAR TAREFA")
        print("2 - VISUALIZAR TAREFAS")
        print("3 - ATUALIZAR TAREFA")
        print("4 - EXCLUIR TAREFA")
        # print("5 - SAIR)

        try:
            opcao = int(input("Escolha a ação que deseja executar: "))
            print("\n")
        except ValueError:
            print("Digite uma opção válida!")

        if opcao == 1:
            criar_atividade(atividades)

        elif opcao == 2:
            visualizar_atividades(atividades)
