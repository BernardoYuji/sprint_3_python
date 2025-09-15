# Dicionario de exemplo

tabela = {
    "time 1": {"jogos": 1, "vitória": 1, "empate": 0, "derrota": 0, "pontos": 3},
    "time 2": {"jogos": 1, "vitória": 0, "empate": 0, "derrota": 1, "pontos": 0},
    "time 3": {"jogos": 1, "vitória": 0, "empate": 1, "derrota": 0, "pontos": 1},
    "time 4": {"jogos": 1, "vitória": 0, "empate": 1, "derrota": 0, "pontos": 1},
    "time 5": {"jogos": 1, "vitória": 1, "empate": 0, "derrota": 0, "pontos": 3},
    "time 6": {"jogos": 1, "vitória": 0, "empate": 0, "derrota": 1, "pontos": 0},
    "time 7": {"jogos": 1, "vitória": 0, "empate": 1, "derrota": 0, "pontos": 1},
    "time 8": {"jogos": 1, "vitória": 0, "empate": 1, "derrota": 0, "pontos": 1}
}


# Função que define o time campeão
def definir_time_campeao(tabela):
    # Encontra a maior pontuação
    maior_pontuacao = max(time["pontos"] for time in tabela.values())

    # Filtra os times que têm essa pontuação
    candidatos = {nome: dados for nome, dados in tabela.items() if dados["pontos"] == maior_pontuacao}

    # Se só tem um, já é o campeão
    if len(candidatos) == 1:
        campeao = list(candidatos.keys())[0]
        print(f"🏆 O time campeão é: {campeao} com {maior_pontuacao} pontos!")
        return

    # Função de desempate
    def desempatar(times):
        # Ordena primeiro por vitórias, depois por menos derrotas
        return sorted(
            times.items(),
            key=lambda item: (item[1]["vitória"], -item[1]["derrota"]),
            reverse=True
        )

    # Aplica o desempate
    desempate = desempatar(candidatos)

    # Pega o 1º colocado após desempate
    melhor_time, melhor_dados = desempate[0]

    # Verifica se ainda empatou com o 2º
    if len(desempate) > 1 and melhor_dados["vitória"] == desempate[1][1]["vitória"] and melhor_dados["derrota"] == desempate[1][1]["derrota"]:
        print(f"🏆 Houve empate total! Times campeões:")
        for time, _ in desempate:
            print(f"- {time}")
    else:
        print(f"🏆 O time campeão é: {melhor_time} com {maior_pontuacao} pontos, {melhor_dados['vitória']} vitórias e {melhor_dados['derrota']} derrotas.")
