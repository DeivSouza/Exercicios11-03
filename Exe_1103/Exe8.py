#8 Escreva um programa que leia a idade de um indivíduo e escreva a faixa etária a que pertence, de acordo com a tabela abaixo;
#Faixa etária - Classificação
# <12 - Criança
# 13~17 - Adolescente
# 18^59 - Adulto
# >60 - Especialista

idade = int(input("Informe sua idade: "))

if idade < 12:
    print("Faixa etária: CRIANÇA")
elif idade >= 12 and idade < 18:
    print("Faixa etária: ADOLESCENTE")
elif idade >= 18 and idade < 60:
    print("Faixa etária: ADULTO")
elif idade >= 60:
    print("Faixa etária: ESPECIALISTA")