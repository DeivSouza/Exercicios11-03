#2 Faça um programa que converta a moeda REAL em DÓLAR
cotacao = 5.81

real = float(input("Informe o valor em Real(R$): "))

dolar = real/cotacao

print(f"O valor em dolares (U$) é: {round(dolar, 2)}")