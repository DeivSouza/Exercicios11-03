#7 Faça um programa que receba o mês em número e apresente-o por extenso.

meses = ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"]

mes_atual = int(input("Informe o Nº do mês: "))

print(f"O mês escolhido foi: {meses[mes_atual - 1]}")

