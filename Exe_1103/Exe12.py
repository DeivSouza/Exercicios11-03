#12 Escreva um algoritmo que a partir da massa e da altura informados pelo usuário, calcule e apresente seu IMC
# e sua classificação conforme a tabela abaixo:
#IMC - Classificação
#< 18 - Magreza
#18 ~ 24,9 - Saudável
#25 ~ 29,9 - Sobrepeso
#>= 30 - Obesidade

peso = float(input("Informe seu pedo (KG): "))
altura = float(input("Informe sua altura: "))

imc = peso / (altura ** 2)

if imc < 18:
    print(f"Seu IMC é {round(imc, 2)}: Magreza")
elif imc >= 18 and imc < 25:
    print(f"Seu IMC é {round(imc, 2)}: Saudável")
elif imc >= 25 and imc < 30:
    print(f"Seu IMC é {round(imc, 2)}: Sobrepeso")
elif imc >= 30:
    print(f"Seu IMC é {round(imc, 2)}: Obeso")