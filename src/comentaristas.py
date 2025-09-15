# Função que recebe a quantidade e nome das comentaristas
def receber_comentaristas():
    quantidade = int(input("Digite o número de comentaristas: "))
    comentaristas = []
    for i in range(quantidade):
        nome = input(f"Digite o nome da {i+1} comentarista: ")
        comentaristas.append(nome)
    return comentaristas

# Função que retorna a lista formatada das comentaristas
def anuncia_comentaristas(lista_comentaristas):
    linhas = ["\nAs comentaristas são:"]
    linhas += [f"- {nome}" for nome in lista_comentaristas]
    return linhas

# Chama as funções
lista = receber_comentaristas()
linhas = anuncia_comentaristas(lista)

# Exibição opcional
for linha in linhas:
    print(linha)
