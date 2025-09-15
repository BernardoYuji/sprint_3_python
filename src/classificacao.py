# Esse programa so será utilizado após o cadastro dos times terem sido realizados.

# Import de dicionarios
from cadastro import times, criar_time

def registrar_resultado(time1, gols1, time2, gols2):
    criar_time(time1)
    criar_time(time2)

    times[time1]["jogos"] += 1
    times[time2]["jogos"] += 1

    if gols1 > gols2:
        times[time1]["vitória"] += 1
        times[time1]["pontos"] += 3
        times[time2]["derrota"] += 1
    elif gols2 > gols1:
        times[time2]["vitória"] += 1
        times[time2]["pontos"] += 3
        times[time1]["derrota"] += 1
    else:
        times[time1]["empate"] += 1
        times[time2]["empate"] += 1
        times[time1]["pontos"] += 1
        times[time2]["pontos"] += 1

    return times

# ===============================
# Exibição da tabela
# ===============================
def exibir_tabela_ordenada():
    linhas = []
    header = "Time     | Jogos | Vitórias | Empates | Derrotas | Pontos"
    linhas.append(header)
    linhas.append("-" * len(header))

    tabela_ordenada = sorted(
        times.items(),
        key=lambda item: (item[1]['pontos'], item[1]['vitória']),
        reverse=True
    )

    for time, dados in tabela_ordenada:
        linha = (
            f"{time:<9} | {dados['jogos']:>5} | {dados['vitória']:>8} | "
            f"{dados['empate']:>7} | {dados['derrota']:>8} | {dados['pontos']:>6}"
        )
        linhas.append(linha)

    return linhas
