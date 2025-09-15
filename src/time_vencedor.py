# Partidas programadas (apenas como referência)
partidas_programadas = [
    {"partida_id": 1, "time1": "time 1", "time2": "time 2", "data": "2025-09-15"},
    {"partida_id": 2, "time1": "time 3", "time2": "time 4", "data": "2025-09-16"},
    {"partida_id": 3, "time1": "time 5", "time2": "time 6", "data": "2025-09-17"},
    {"partida_id": 4, "time1": "time 7", "time2": "time 8", "data": "2025-09-18"}
]

# Resultados das partidas
resultado_partidas = {
    1: {"time 1": 2, "time 2": 1},
    2: {"time 3": 0, "time 4": 0},
    3: {"time 5": 3, "time 6": 2},
    4: {"time 7": 1, "time 8": 4}
}

# Tabela de classificação
tabela = {
    "time 1": {"jogos": 0, "vitória": 0, "empate": 0, "derrota": 0, "pontos": 0},
    "time 2": {"jogos": 0, "vitória": 0, "empate": 0, "derrota": 0, "pontos": 0},
    "time 3": {"jogos": 0, "vitória": 0, "empate": 0, "derrota": 0, "pontos": 0},
    "time 4": {"jogos": 0, "vitória": 0, "empate": 0, "derrota": 0, "pontos": 0},
    "time 5": {"jogos": 0, "vitória": 0, "empate": 0, "derrota": 0, "pontos": 0},
    "time 6": {"jogos": 0, "vitória": 0, "empate": 0, "derrota": 0, "pontos": 0},
    "time 7": {"jogos": 0, "vitória": 0, "empate": 0, "derrota": 0, "pontos": 0},
    "time 8": {"jogos": 0, "vitória": 0, "empate": 0, "derrota": 0, "pontos": 0}
}

# Função que atualiza a tabela com base no resultado
def atualizar_tabela(resultados, tabela):
    for partida_id, resultado in resultados.items():
        times = list(resultado.keys())
        time1 = times[0]
        time2 = times[1]
        gols1 = resultado[time1]
        gols2 = resultado[time2]

        print(f"Resultado da partida {partida_id}: {time1} {gols1} x {gols2} {time2}")

        tabela[time1]["jogos"] += 1
        tabela[time2]["jogos"] += 1

        if gols1 > gols2:
            tabela[time1]["vitória"] += 1
            tabela[time2]["derrota"] += 1
            tabela[time1]["pontos"] += 3
            vencedor = time1
        elif gols1 < gols2:
            tabela[time2]["vitória"] += 1
            tabela[time1]["derrota"] += 1
            tabela[time2]["pontos"] += 3
            vencedor = time2
        else:
            tabela[time1]["empate"] += 1
            tabela[time2]["empate"] += 1
            tabela[time1]["pontos"] += 1
            tabela[time2]["pontos"] += 1
            vencedor = "empate"

        print(f"Vencedor da partida {partida_id}: {vencedor}\n")

# Executar
atualizar_tabela(resultado_partidas, tabela)

# Mostrar tabela final
import pprint
print("Tabela atualizada:")
pprint.pprint(tabela)
