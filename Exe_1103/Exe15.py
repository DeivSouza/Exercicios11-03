#15 Faça um programa que calcule a tabuada de um número digitado pelo usuário;

tabuada = int(input("Qual tabuada deseja saber? "))

for i in range (11):
    print(f"{tabuada} x {i} = {tabuada * i}")