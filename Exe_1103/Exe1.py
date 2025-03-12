#1 Faça um programa que receba 5 notas, calcule a média aritmética destas notas e apresente o resultado.

soma = 0
media = 0

n1 = float(input("Insira a N1: "))
n2 = float(input("Insira a N2: "))
n3 = float(input("Insira a N3: "))
n4 = float(input("Insira a N4: "))
n5 = float(input("Insira a N5: "))

soma = n1 + n2 + n3 + n4 + n5
media = soma/5

print(f"Sua média é: {media}")