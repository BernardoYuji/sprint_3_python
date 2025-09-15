# Função que retorna a lista de organizadoras
def receber_organizadoras():
    return ["Passa a Bola"]  # única organizadora

# Função que retorna a lista formatada das organizadoras
def anuncia_organizadoras(lista_organizadoras):
    linhas = ["\nA organizadora do evento é:"]
    linhas += [f"- {nome}" for nome in lista_organizadoras]
    return linhas

# Chama as funções
lista = receber_organizadoras()
linhas = anuncia_organizadoras(lista)

# Exibição opcional
for linha in linhas:
    print(linha)
