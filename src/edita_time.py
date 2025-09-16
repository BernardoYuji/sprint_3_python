# Import de dados do cadastro.py

from cadastro import times, jogadoras_ordenadas, estatisticas_jogadoras


# Função para editar informações de uma jogadora já cadastrada
def editar_jogadora(nome_jogadora, novo_nome=None, nova_posicao=None, novo_time=None):
    if nome_jogadora not in jogadoras_ordenadas:
        return f"Jogadora {nome_jogadora} não encontrada."

    info_atual = jogadoras_ordenadas[nome_jogadora]
    time_atual = info_atual["time"]
    vaga = info_atual["vaga"]

    # Atualiza nome da jogadora
    if novo_nome:
        # Atualiza no dicionário jogadoras_ordenadas
        jogadoras_ordenadas[novo_nome] = jogadoras_ordenadas.pop(nome_jogadora)
        jogadoras_ordenadas[novo_nome]["vaga"] = vaga
        jogadoras_ordenadas[novo_nome]["time"] = time_atual
        # Atualiza no time
        times[time_atual]["jogadoras"][vaga] = novo_nome
        # Atualiza estatísticas, se já existir
        if nome_jogadora in estatisticas_jogadoras:
            estatisticas_jogadoras[novo_nome] = estatisticas_jogadoras.pop(nome_jogadora)
        nome_jogadora = novo_nome

    # Atualiza posição
    if nova_posicao:
        jogadoras_ordenadas[nome_jogadora]["posição"] = nova_posicao

    # Atualiza para um novo time
    if novo_time and novo_time != time_atual:
        from cadastro import criar_time
        criar_time(novo_time)

        # Remove do time antigo
        times[time_atual]["jogadoras"][vaga] = ""

        # Encontra uma vaga livre no novo time
        for vaga_nova in times[novo_time]["jogadoras"]:
            if times[novo_time]["jogadoras"][vaga_nova] == "":
                times[novo_time]["jogadoras"][vaga_nova] = nome_jogadora
                jogadoras_ordenadas[nome_jogadora]["time"] = novo_time
                jogadoras_ordenadas[nome_jogadora]["vaga"] = vaga_nova
                break
        else:
            return f"O time {novo_time} não possui vagas disponíveis."

    return f"Jogadora {nome_jogadora} editada com sucesso!"


# Função para remover uma jogadora de um time
def remover_jogadora(nome_jogadora):
    if nome_jogadora not in jogadoras_ordenadas:
        return f"Jogadora {nome_jogadora} não encontrada."

    info = jogadoras_ordenadas.pop(nome_jogadora)
    time = info["time"]
    vaga = info["vaga"]

    # Remove do time
    times[time]["jogadoras"][vaga] = ""

    # Remove estatísticas, se existirem
    if nome_jogadora in estatisticas_jogadoras:
        estatisticas_jogadoras.pop(nome_jogadora)

    return f"Jogadora {nome_jogadora} removida com sucesso!"


# Teste 
if __name__ == "__main__":
    print("=== Edição de Jogadoras ===")
    nome = input("Digite o nome da jogadora que deseja editar: ")

    acao = input("Deseja [editar] ou [remover] a jogadora? ")

    if acao == "editar":
        novo_nome = input("Novo nome (ou Enter para manter): ") or None
        nova_posicao = input("Nova posição (ou Enter para manter): ") or None
        novo_time = input("Novo time (ou Enter para manter): ") or None
        print(editar_jogadora(nome, novo_nome, nova_posicao, novo_time))

    elif acao == "remover":
        print(remover_jogadora(nome))
