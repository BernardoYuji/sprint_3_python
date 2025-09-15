# Função que verifica as quadras disponíveis

def verificar_quadras_disponiveis(quadras):
    
    livres = []
    for i, ocupada in enumerate(quadras):
        if not ocupada:
            livres.append(i + 1)  # +1 para numerar quadras a partir de 1
    return livres

# Exemplo
quantidade_quadras = 4
# False = livre, True = ocupada
quadras = [True, False, False, True]

quadras_livres = verificar_quadras_disponiveis(quadras)
if quadras_livres:
    print(f"Quadras disponíveis: {quadras_livres}")
    print(f"A primeira quadra livre é a quadra {quadras_livres[0]}")
else:
    print("Nenhuma quadra disponível no momento.")
