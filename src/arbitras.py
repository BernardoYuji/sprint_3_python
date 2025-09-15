# Função para receber árbitras
def receber_arbitras():
    quantidade = int(input("Digite o número de árbitras: "))
    arbitras = []
    for i in range(quantidade):
        nome = input(f"Digite o nome da {i+1} árbitra: ")
        arbitras.append(nome)
    return arbitras

# Função que retorna a lista formatada das árbitras
def anuncia_arbitras(lista_arbitras):
    # Retorna uma lista de strings formatadas
    return [f"- {nome}" for nome in lista_arbitras]

# Chamada das funções
lista = receber_arbitras()
resultado = anuncia_arbitras(lista)

# Se quiser imprimir, você pode fazer:
print("\nAs árbitras são:")
for linha in resultado:
    print(linha)
