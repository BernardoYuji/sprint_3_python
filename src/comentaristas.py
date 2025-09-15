# Função que recebe a quantidade e nome das comentaristas

def receber_comentaristas():
    quantidade = int(input("Digite o número de comentaristas"))
    comentaristas = []
    for i in range(quantidade):
        nome = input(f"Digite o nome da {i+1} comentarista: ")
        comentaristas.append(nome)
    return comentaristas

# Funçâo que anuncia as comentaristas

def anuncia_comentaristas(lista_comentaristas):
    print("\nAs comentaristas são: ")
    for nome in lista_comentaristas:
        print(f"- {nome}")


# Chama as funções
lista = receber_comentaristas()
anuncia_comentaristas(lista)