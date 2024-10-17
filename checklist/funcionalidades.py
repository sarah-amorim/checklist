from limpar_tela.limpar_tela import limpar_tela


def criar_atividade(array_atividades):
    titulo = input("Digite o título da atividade: ")
    descricao = input("Digite a descrição da atividade: ")
    data = input("Digite a data de conclusão (dd/mm/aaaa): ")
    status = input("A atividade está concluída? (sim/não): ").lower()

    atividade = {
        "titulo": titulo,
        "descricao": descricao,
        "data": data,
        "status": status == "sim"
    }

    array_atividades.append(atividade)
    print("Atividade criada com sucesso!")
    limpar_tela()


def visualizar_atividades(array_atividades):
    if not array_atividades:
        print("Nenhuma atividade encontrada.")
        return

    for i, atividade in enumerate(array_atividades, start=1):
        status = "Concluída" if atividade["status"] else "Pendente"
        print(f"{i}. {atividade['titulo']} - {status}")
        print(f"   Descrição: {atividade['descricao']}")
        print(f"   Data de Conclusão: {atividade['data']}\n")


def atualizar_atividade(array_atividades):
    visualizar_atividades(array_atividades)

    if not array_atividades:
        return

    indice = int(input("Digite o número da atividade que deseja atualizar: "))
    indice -= 1

    if 0 <= indice < len(array_atividades):
        titulo = input("Digite o novo título da atividade (ou pressione Enter para manter): ")
        descricao = input("Digite a nova descrição da atividade (ou pressione Enter para manter): ")
        data = input("Digite a nova data de conclusão (dd/mm/aaaa) (ou pressione Enter para manter): ")
        status = input("A atividade está concluída? (sim/não) (ou pressione Enter para manter): ")

        if titulo:
            array_atividades[indice]["titulo"] = titulo
        if descricao:
            array_atividades[indice]["descricao"] = descricao
        if data:
            array_atividades[indice]["data"] = data
        if status.lower() in ["sim", "não"]:
            array_atividades[indice]["status"] = status.lower() == "sim"

        print("Atividade atualizada com sucesso!")
    else:
        print("Índice inválido!")


def deletar_tarefas(array_atividades):
    visualizar_atividades(array_atividades)

    try:
        indice = int(input("Digite o índice da tarefa que deseja excluir: "))
    except ValueError:
        print("Digite uma opção válida!")

    indice_ajustado = indice - 1

    if 0 <= indice_ajustado < len(array_atividades):
        array_atividades.pop(indice_ajustado)
        print("Atividade excluida!")
    else:
        print("Índice inválido!")
