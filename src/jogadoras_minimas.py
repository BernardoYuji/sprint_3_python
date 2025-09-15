#Import dos times 
from cadastro import times

# Função que verifica se o time possui o número minimo de jogadoras
def verificar_jogadoras_minimas(minimo=8):
    for nome_time, dados in times.items():
        preenchidas = [j for j in dados["jogadoras"].values() if j.strip() != ""]
        if len(preenchidas) < minimo:
            print(f"{nome_time}: Jogadoras insuficientes ({len(preenchidas)}/{minimo})")
        else:
            print(f"{nome_time}: Time pode se cadastrar ({len(preenchidas)}/{minimo})")

# Teste
if __name__ == "__main__":
    verificar_jogadoras_minimas()
