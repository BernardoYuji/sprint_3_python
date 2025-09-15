# Dicionário de estatísticas
estatisticas_jogadoras = {}

# Dicionário de times (inicia vazio)
times = {}

# Dicionário para armazenar todas as jogadoras em ordem alfabética
jogadoras_ordenadas = {}

# Função para garantir que o time exista (se não existir, cria)
def criar_time(time):
    if time not in times:
        times[time] = {f"jogadora{i}": "" for i in range(1, 9)}

# Função para cadastrar jogadora no primeiro espaço vazio de um time
def cadastrar_jogadora(time, nome_jogadora, posicao):
    criar_time(time)
    for vaga in times[time]:
        if times[time][vaga] == "":
            times[time][vaga] = nome_jogadora
            jogadoras_ordenadas[nome_jogadora] = {"time": time, "vaga": vaga, "posição": posicao}
            print(f"{nome_jogadora} cadastrada no {time} na {vaga} ({posicao})")
            return True
    print("Todas as posições já estão preenchidas nesse time.")
    return False

# Função para cadastrar estatísticas da jogadora
def cadastrar_estatisticas(nome, gols, assistencias, cartoes_amarelo, cartoes_vermelho):
    estatisticas_jogadoras[nome] = {
        "gols": gols,
        "assistências": assistencias,
        "cartões amarelos": cartoes_amarelo,
        "cartões vermelhos": cartoes_vermelho
    }

# Função para mostrar jogadoras em ordem alfabética
def mostrar_jogadoras_ordenadas():
    print("\n=== Jogadoras em ordem alfabética ===")
    for nome in sorted(jogadoras_ordenadas.keys()):
        info = jogadoras_ordenadas[nome]
        print(f"{nome} - Time: {info['time']}, {info['vaga']} ({info['posição']})")

# Função para mostrar as 5 jogadoras com mais gols
def mostrar_top_gols():
    print("\n=== Top 5 jogadoras com mais gols ===")
    top_gols = sorted(estatisticas_jogadoras.items(), key=lambda item: item[1]["gols"], reverse=True)
    for i, (nome, stats) in enumerate(top_gols[:5], start=1):
        print(f"{i}. {nome} - {stats['gols']} gols")


print("Cadastro de nova jogadora!")

nome = input("Digite o nome da jogadora: ")
posicao = input("Digite a posição da jogadora: ")
gols = int(input("Digite a quantidade de gols marcados: "))
assistencias = int(input("Digite a quantidade de assistências: "))
cartoes_amarelo = int(input("Digite a quantidade de cartões amarelos: "))
cartoes_vermelho = int(input("Digite a quantidade de cartões vermelhos: "))
time_escolhido = input("Digite o nome do time para cadastrar a jogadora: ")

# Cadastro
if cadastrar_jogadora(time_escolhido, nome, posicao):
    cadastrar_estatisticas(nome, gols, assistencias, cartoes_amarelo, cartoes_vermelho)

# Mostrar sempre depois
mostrar_jogadoras_ordenadas()
mostrar_top_gols()
