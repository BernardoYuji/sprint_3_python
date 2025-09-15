# verificacao.py
from cadastro import times

# Função para verificar se o time tem jogadoras suficientes
def verificar_jogadoras_minimas(times, minimo=8):
    for nome_time, dados_time in times.items():
        # Conta apenas as jogadoras com nome preenchido
        preenchidas = [nome for nome in dados_time["jogadoras"].values() if nome.strip() != ""]
        
        if len(preenchidas) < minimo:
            print(f"{nome_time}: Jogadoras insuficientes ({len(preenchidas)}/{minimo})")
        else:
            print(f"{nome_time}: Time pode se cadastrar ({len(preenchidas)}/{minimo})")

# Chama a função
verificar_jogadoras_minimas(times)
