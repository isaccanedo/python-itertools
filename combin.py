import itertools

# Conjunto inicial
conjunto = [1, 2, 3, 4, 5]

# Gerar todas as combinações de 2 elementos
combinacoes = list(itertools.combinations(conjunto, 2))

# Imprimir as combinações
for combinacao in combinacoes:
    print(combinacao)
