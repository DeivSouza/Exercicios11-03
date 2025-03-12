#11 Escreva um algoritmo para exibir o nome do lanche a partir da entrada do número do mesmo pelo usuário, de acordo com a tabela abaixo:

lanche = ["Big Mac", "Quarteirão", "McChicken", "Cheddar McMelt", "McMax"]

pedido = int(input("Nº do pedido: "))

print(lanche[pedido - 1])