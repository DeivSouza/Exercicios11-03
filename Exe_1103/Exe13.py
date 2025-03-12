#13 Faça um programa que receba 3 valores e verifique se eles podem representar os lados em um triângulo;
# Nome - Característica
#Equilátero - 3 lados iguais
#Isósceles - 2 lados iguais
#Escaleno - 3 lados diferente

valor1 = float(input("Digite lado 1: "))
valor2 = float(input("Digite lado 2: "))
valor3 = float(input("Digite lado 3: "))

if valor1 == valor2 and valor1 == valor3:
    print("É possível montar um triângulo EQUILÁTERO")
elif valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
    print("É possível montar um triânculo ISÓSELES")
else:
    print("É possível montar um triânculo ESCALENO")