#17 Faça um programa que receba dois valores, sendo que o primeiro deve ser menor que o segundo.
# O programa deve apresentar todos os números ímpares contidos nesta sequência. (Modulo %. Exemplo: 7%2 = 1)

num1 = int(input("Nº1: "))
num2 = int(input("Nº2: "))

if num2 <= num1:
    print("Nº2 Deve ser maior que o Nº1")
for i in range (num1, num2 + 1):
    if i % 2 == 1:
        print(i)