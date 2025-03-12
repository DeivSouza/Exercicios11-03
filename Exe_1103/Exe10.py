#10 Escreva um programa que leia a velocidade máxima permitida em uma avenida e velocidade com que o motorista estava dirigindo nela
# e calcule a multa que uma pessoa vai receber;
#Velocidade Ultrapassada - Valor da Multa
#Até 10 km/h - R$ 50,00
#11 a 30 km/h - R$ 100,00
#Mais 31 km/h - R$ 200,00

vel_permitida = float(input("Velocidade Máxima Permitida (KM/h): "))
vel_veiculo = float(input("Velocidade do Veículo: "))

if vel_veiculo <= vel_permitida:
    print("SEM APLICAÇÃO DE MULTA")
elif vel_veiculo - vel_permitida > 0 and vel_veiculo - vel_permitida < 10:
    print("Multa aplicada: R$50,00")
elif vel_veiculo - vel_permitida >= 11 and vel_veiculo - vel_permitida <31:
    print("Mulpta aplicada: R$100,00")
elif vel_veiculo - vel_permitida >= 30:
    print("Multa aplicada: R$200,00")