import funções
pessoas = []
for pessoa in range(1,6):
    pessoas.append(float(input(f"digite o peso da {pessoa} pessoa: ")))
funções.maior(pessoas)
funções.menor(pessoas)

