# Função que recebe a quantidade e nome das arbitras presente no evento


def receber_arbitras():
    quantidade = int(input("Digite o número de Árbitras"))
    arbitras = []
    for i in range(quantidade):
        nome = input(f"Digite o nome da {i+1} arbitra: ")
        arbitras.append(nome)
    return arbitras

# Função que anuncia as arbitras 

def anuncia_arbitras(lista_arbitras):
    print("\nAs árbitras são: ")
    for nome in lista_arbitras:
        print(f"- {nome}")

# Chama as funções
lista = receber_arbitras()
anuncia_arbitras(lista)