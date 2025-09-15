# Tabela começa vazia
tabela = {}

# Função para criar um time na tabela (se não existir)
def criar_time_tabela(nome_time):
    if nome_time not in tabela:
        tabela[nome_time] = {
            "jogos": 0,
            "vitória": 0,
            "empate": 0,
            "derrota": 0,
            "pontos": 0
        }

# Função para registrar resultado de uma partida
def registrar_resultado(time1, gols1, time2, gols2):
    criar_time_tabela(time1)
    criar_time_tabela(time2)

    # Cada time jogou uma vez
    tabela[time1]["jogos"] += 1
    tabela[time2]["jogos"] += 1

    if gols1 > gols2:  # vitória do time1
        tabela[time1]["vitória"] += 1
        tabela[time1]["pontos"] += 3
        tabela[time2]["derrota"] += 1

    elif gols2 > gols1:  # vitória do time2
        tabela[time2]["vitória"] += 1
        tabela[time2]["pontos"] += 3
        tabela[time1]["derrota"] += 1

    else:  # empate
        tabela[time1]["empate"] += 1
        tabela[time2]["empate"] += 1
        tabela[time1]["pontos"] += 1
        tabela[time2]["pontos"] += 1

# Função para exibir a tabela ordenada
def exibir_tabela_ordenada():
    print("Time     | Jogos | Vitórias | Empates | Derrotas | Pontos")
    print("-----------------------------------------------------------")

    tabela_ordenada = sorted(
        tabela.items(),
        key=lambda item: (item[1]['pontos'], item[1]['vitória']),
        reverse=True
    )

    for time, dados in tabela_ordenada:
        print(f"{time:<9} | {dados['jogos']:>5} | {dados['vitória']:>8} | {dados['empate']:>7} | {dados['derrota']:>8} | {dados['pontos']:>6}")


# Exemplo 


registrar_resultado("time 1", 2, "time 2", 1)  # time1 ganhou
registrar_resultado("time 3", 0, "time 4", 0)  # empate
registrar_resultado("time 5", 3, "time 6", 1)  # time5 ganhou
registrar_resultado("time 5", 2, "time 7", 0)  # time5 ganhou de novo
registrar_resultado("time 8", 1, "time 7", 1)  # empate


# Chama a função
exibir_tabela_ordenada()
