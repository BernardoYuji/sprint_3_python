# Dicionário de estatísticas individuais das jogadoras
estatisticas_jogadoras = {}

# Dicionário de times (inicia vazio)
times = {}

# Dicionário para armazenar todas as jogadoras em ordem alfabética
jogadoras_ordenadas = {}


# Função para garantir que o time exista (se não existir, cria com estatísticas zeradas)
def criar_time(time):
    if time not in times:
        times[time] = {
            "jogadoras": {f"jogadora{i}": "" for i in range(1, 9)},
            "jogos": 0,
            "vitória": 0,
            "empate": 0,
            "derrota": 0,
            "pontos": 0
        }
    return times[time]


# Função para cadastrar jogadora no primeiro espaço vazio de um time
def cadastrar_jogadora(time, nome_jogadora, posicao):
    criar_time(time)
    for vaga in times[time]["jogadoras"]:
        if times[time]["jogadoras"][vaga] == "":
            times[time]["jogadoras"][vaga] = nome_jogadora
            jogadoras_ordenadas[nome_jogadora] = {
                "time": time,
                "vaga": vaga,
                "posição": posicao
            }
            return f"{nome_jogadora} cadastrada no {time} na {vaga} ({posicao})"
    return "Todas as posições já estão preenchidas nesse time."


# Função para cadastrar estatísticas da jogadora
def cadastrar_estatisticas(nome, gols, assistencias, cartoes_amarelo, cartoes_vermelho):
    estatisticas_jogadoras[nome] = {
        "gols": gols,
        "assistências": assistencias,
        "cartões amarelos": cartoes_amarelo,
        "cartões vermelhos": cartoes_vermelho
    }
    return estatisticas_jogadoras[nome]


# Função para registrar resultado de um time
def registrar_resultado(time, vitoria=False, empate=False, derrota=False):
    criar_time(time)
    times[time]["jogos"] += 1
    if vitoria:
        times[time]["vitória"] += 1
        times[time]["pontos"] += 3
    elif empate:
        times[time]["empate"] += 1
        times[time]["pontos"] += 1
    elif derrota:
        times[time]["derrota"] += 1
    return times[time]


# Função para retornar jogadoras em ordem alfabética
def mostrar_jogadoras_ordenadas():
    jogadoras = []
    for nome in sorted(jogadoras_ordenadas.keys()):
        info = jogadoras_ordenadas[nome]
        jogadoras.append(f"{nome} - Time: {info['time']}, {info['vaga']} ({info['posição']})")
    return jogadoras


# Função para retornar as 5 jogadoras com mais gols
def mostrar_top_gols():
    top_gols = sorted(estatisticas_jogadoras.items(), key=lambda item: item[1]["gols"], reverse=True)
    ranking = []
    for i, (nome, stats) in enumerate(top_gols[:5], start=1):
        ranking.append(f"{i}. {nome} - {stats['gols']} gols")
    return ranking


# Teste
if __name__ == "__main__":
    print("Cadastro de nova jogadora!")

    nome = input("Digite o nome da jogadora: ")
    posicao = input("Digite a posição da jogadora: ")
    gols = int(input("Digite a quantidade de gols marcados: "))
    assistencias = int(input("Digite a quantidade de assistências: "))
    cartoes_amarelo = int(input("Digite a quantidade de cartões amarelos: "))
    cartoes_vermelho = int(input("Digite a quantidade de cartões vermelhos: "))
    time_escolhido = input("Digite o nome do time para cadastrar a jogadora: ")

    # Cadastro
    print(cadastrar_jogadora(time_escolhido, nome, posicao))
    cadastrar_estatisticas(nome, gols, assistencias, cartoes_amarelo, cartoes_vermelho)

    # Exemplo de resultado (só para testar)
    registrar_resultado(time_escolhido, vitoria=True)

    # Mostrar sempre depois
    print("\n=== Jogadoras em ordem alfabética ===")
    for j in mostrar_jogadoras_ordenadas():
        print(j)

    print("\n=== Top 5 jogadoras com mais gols ===")
    for j in mostrar_top_gols():
        print(j)

    print("\nTabela de times:")
    print(times)
