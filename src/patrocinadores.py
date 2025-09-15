# Função que recebe a quantidade e o nome dos patrocinadores
def receber_patrocinadores():
    quantidade = int(input("Digite o número de patrocinadores: "))
    patrocinadores = []
    for i in range(quantidade):
        nome = input(f"Digite o nome do {i+1}º patrocinador: ")
        patrocinadores.append(nome)
    return patrocinadores

# Função que retorna a lista formatada dos patrocinadores
def anuncia_patrocinadores(lista_patrocinadores):
    linhas = ["\nOs patrocinadores são:"]
    linhas += [f"- {nome}" for nome in lista_patrocinadores]
    return linhas

# Chama as funções
lista = receber_patrocinadores()
linhas = anuncia_patrocinadores(lista)

# Exibição opcional
for linha in linhas:
    print(linha)
