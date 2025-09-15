from cadastro import times

def definir_time_campeao():
    # Encontra a maior pontuação
    maior_pontuacao = max(time["pontos"] for time in times.values())

    # Filtra os times que têm essa pontuação
    candidatos = {
        nome: dados for nome, dados in times.items()
        if dados["pontos"] == maior_pontuacao
    }

    # Se só tem um, já é o campeão
    if len(candidatos) == 1:
        campeao = list(candidatos.keys())[0]
        return f"🏆 O time campeão é: {campeao} com {maior_pontuacao} pontos!"

    # Função de desempate
    def desempatar(times_dict):
        # Ordena primeiro por vitórias, depois por menos derrotas
        return sorted(
            times_dict.items(),
            key=lambda item: (item[1]["vitória"], -item[1]["derrota"]),
            reverse=True
        )

    # Aplica o desempate
    desempate = desempatar(candidatos)

    # Pega o 1º colocado após desempate
    melhor_time, melhor_dados = desempate[0]

    # Verifica se ainda empatou com o 2º
    if (
        len(desempate) > 1
        and melhor_dados["vitória"] == desempate[1][1]["vitória"]
        and melhor_dados["derrota"] == desempate[1][1]["derrota"]
    ):
        # Retorna todos empatados
        campeoes = [time for time, _ in desempate]
        return ["🏆 Houve empate total! Times campeões:"] + campeoes
    else:
        return (
            f"🏆 O time campeão é: {melhor_time} com {maior_pontuacao} pontos, "
            f"{melhor_dados['vitória']} vitórias e {melhor_dados['derrota']} derrotas."
        )
from cadastro import times

def definir_time_campeao():
    # Encontra a maior pontuação
    maior_pontuacao = max(time["pontos"] for time in times.values())

    # Filtra os times que têm essa pontuação
    candidatos = {
        nome: dados for nome, dados in times.items()
        if dados["pontos"] == maior_pontuacao
    }

    # Se só tem um, já é o campeão
    if len(candidatos) == 1:
        campeao = list(candidatos.keys())[0]
        return f"🏆 O time campeão é: {campeao} com {maior_pontuacao} pontos!"

    # Função de desempate
    def desempatar(times_dict):
        # Ordena primeiro por vitórias, depois por menos derrotas
        return sorted(
            times_dict.items(),
            key=lambda item: (item[1]["vitória"], -item[1]["derrota"]),
            reverse=True
        )

    # Aplica o desempate
    desempate = desempatar(candidatos)

    # Pega o 1º colocado após desempate
    melhor_time, melhor_dados = desempate[0]

    # Verifica se ainda empatou com o 2º
    if (
        len(desempate) > 1
        and melhor_dados["vitória"] == desempate[1][1]["vitória"]
        and melhor_dados["derrota"] == desempate[1][1]["derrota"]
    ):
        # Retorna todos empatados
        campeoes = [time for time, _ in desempate]
        return ["🏆 Houve empate total! Times campeões:"] + campeoes
    else:
        return (
            f"🏆 O time campeão é: {melhor_time} com {maior_pontuacao} pontos, "
            f"{melhor_dados['vitória']} vitórias e {melhor_dados['derrota']} derrotas."
        )
