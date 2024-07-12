# Define uma lista com os valores das notas disponíveis
notas = [100, 50, 10, 5, 1]

# Solicita ao usuário que insira um valor e converte o valor de entrada para inteiro
valor = int(input("Digite o valor: "))

# Inicializa um dicionário para armazenar a quantidade de cada nota necessária
quantidade_notas = {}

# Itera sobre cada valor de nota na lista
for nota in notas:
    # Calcula quantas notas do valor atual são necessárias e atualiza o valor restante
    quantidade_notas[nota], valor = divmod(valor, nota)

# Imprime um cabeçalho para os resultados
print("Notas necessárias:")

# Itera sobre o dicionário de resultados e imprime a quantidade de cada nota
for nota, quantidade in quantidade_notas.items():
    print(f"Notas de {nota}: {quantidade}")
