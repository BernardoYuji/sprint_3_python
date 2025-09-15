# Dicionário dos times com jogadoras
times = {
    "time1": {
        "jogadora1": "Ana",
        "jogadora2": "Bia",
        "jogadora3": "Carla",
        "jogadora4": "Duda",
        "jogadora5": "Eva",
        "jogadora6": "Fabi",
        "jogadora7": "Gabi",
        "jogadora8": "Helena"
    },
    "time2": {
        "jogadora1": "Isa",
        "jogadora2": "Ju",
        "jogadora3": "Karen",
        "jogadora4": "",  # Vazia
        "jogadora5": "",
        "jogadora6": "",
        "jogadora7": "",
        "jogadora8": ""
    }
}

# Função para verificar se o time tem jogadoras suficientes
def verificar_jogadoras_minimas(times, minimo=8):
    for nome_time, jogadoras in times.items():
        # Conta apenas as jogadoras com nome preenchido
        preenchidas = [nome for nome in jogadoras.values() if nome.strip() != ""]
        
        if len(preenchidas) < minimo:
            print(f"{nome_time}: Jogadoras insuficientes ({len(preenchidas)}/{minimo})")
        else:
            print(f"{nome_time}: Time pode se cadastrar ({len(preenchidas)}/{minimo})")

# Chama a função
verificar_jogadoras_minimas(times)
