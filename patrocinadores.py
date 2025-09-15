# Função que recebe a quantidade e o nome dos patrocinadores

def receber_patrocinadores():
    quantidade = int(input("Digite o número de patrocinadores "))
    patrocinadores = []
    for i in range(quantidade):
        nome = input(f"Digite o nome da {i+1} patrocinadores: ")
        patrocinadores.append(nome)
    return patrocinadores


# Função que anuncia os patrocinadores
def anuncia_patrocinadores(lista_patrocinadores):
    print("\nOs patrocinadores são: ")
    for nome in lista_patrocinadores:
        print(f"- {nome}")


#Chama a função
lista = receber_patrocinadores()
anuncia_patrocinadores(lista)