from checklist.funcionalidades import *
from limpar_tela.limpar_tela import limpar_tela

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
        print("5 - SAIR")

        try:
            opcao = int(input("Escolha a ação que deseja executar: "))
        except ValueError:
            limpar_tela()
            print("Digite uma opção válida!\n")
            continue

        if opcao == 1:
            criar_atividade(atividades)
            limpar_tela()

        elif opcao == 2:
            limpar_tela()
            visualizar_atividades(atividades)

        elif opcao == 3:
            atualizar_atividade(atividades)
            limpar_tela()

        elif opcao == 4:
            deletar_tarefas(atividades)
            limpar_tela()

        elif opcao == 5:
            limpar_tela()
            break
