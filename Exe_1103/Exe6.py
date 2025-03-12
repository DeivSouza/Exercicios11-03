#6 Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que:
#Salário < R$ 1000,00 aumento de 25%.
#Salário >= R$ 1000,00 e < R$ 2000,00 aumento de 15%.
#Salário >= R$ 2000,00 aumento de 10%.

salario_atual = float(input("Informe salário atual: R$"))

if salario_atual < 1000:
    print(f"Seu novo salário é: R${salario_atual * 1.25}")
elif salario_atual  >= 1000 and salario_atual < 2000:
    print(f"Seu novo salário é: R${salario_atual * 1.15}")
elif salario_atual >= 2000:
    print(f"Seu novo salário é: R${salario_atual * 1.10}")