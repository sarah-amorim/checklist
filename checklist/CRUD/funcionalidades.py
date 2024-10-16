def criar_atividade(array_atividades):
    titulo = input("Digite o título da atividade: ")
    descricao = input("Digite a descrição da atividade: ")
    data = input("Digite a data de conclusão (dd/mm/aaaa): ")
    status = input("A atividade está concluída? (sim/não): ")

    atividade = {
        "titulo": titulo,
        "descricao": descricao,
        "data": data,
        "status": status.lower() == "sim"  # Armazena True ou False
    }

    array_atividades.append(atividade)
    print("Atividade criada com sucesso!")


def visualizar_atividades(array_atividades):
    if not array_atividades:
        print("Nenhuma atividade encontrada.")
        return

    for i, atividade in enumerate(array_atividades, start=1):
        status = "Concluída" if atividade["status"] else "Pendente"
        print(f"{i}. {atividade['titulo']} - {status}")
        print(f"   Descrição: {atividade['descricao']}")
        print(f"   Data de Conclusão: {atividade['data']}\n")