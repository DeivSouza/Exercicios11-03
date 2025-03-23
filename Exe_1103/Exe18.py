#Faça um programa que receba 10 números e apresente a soma dos números pares e dos números ímpares;

numeros = []
lista_pares = []
lista_impares = []

for i in range (0,10):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

    if numeros[i] % 2 == 0:
       lista_pares.append(numeros[i])
    elif numeros[i] % 2 == 1:
        lista_impares.append(numeros[i])

somapares = sum(lista_pares)
somaimpares = sum(lista_impares)

print("\n")
print(f"Os números digitados foram: {numeros}")
print(f"A soma dos nº PARES digitados é: {somapares}")
print(f"A soma dos nº IMPARES digitados é: {somaimpares}")