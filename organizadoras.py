# Função que retorna a lista de organizadoras
def receber_organizadoras():
    return ["Passa a Bola"]  # única organizadora

# Função que anuncia as organizadoras
def anuncia_organizadoras(lista_organizadoras):
    print("\nA organizadora do evento é: ")
    for nome in lista_organizadoras:
        print(f"- {nome}")


# Chama as funções
lista = receber_organizadoras()
anuncia_organizadoras(lista)
