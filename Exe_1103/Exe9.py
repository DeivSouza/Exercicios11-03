#9 Faça um programa para exibir a ocupação de um funcionário a partir de seu código de profissão, de acordo com a tabela abaixo;
#Código de Profissão - Ocupação
# 1 - Matemático
# 2 - Analista de Sistemas
# 3 - Físico
# 4 - Arquiteto
# 5 - Piloto de Aeronaves

ocupacao = ["Matemático", "Analista de Sistemas", "Físico", "Arquiteto", "Piloto de Aeronaves"]

cod_profissao = int(input("Informe o Cód de Profissão: "))

print("A profissão escolhida é: ", ocupacao[cod_profissao -1])