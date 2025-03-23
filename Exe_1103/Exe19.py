#19 Faça um programa que receba duas notas de seis alunos. Calcule e mostre:
# A média aritmética das duas notas de cada aluno;
# A mensagem que está na tabela a seguir:
#Média Aritmética - Mensagem
#Até 3          - Reprovado
#Entre 3 e 7    - Exame
#De 7 para cima - Aprovado
#O total de alunos aprovados;
#O total de alunos de exame;
#O total de alunos reprovados;
#A média da classe.

total_aprovados = 0
total_exame = 0
total_reprovados = 0
soma_media = 0

for i in range (6):
    nota1 = float(input(f"Digite a 1ª nota do {i+1}º Aluno: "))
    nota2 = float(input(f"Digite a 2ª nota do {i+1}º Aluno: "))

    media = (nota1 + nota2) / 2
    soma_media += media

    print("+-------------------------+")
    print(f"A média do {i+1}º aluno é: {media}")

    if media <= 3:
        print("Aluno REPROVADO!")
    elif media > 3 and media < 7:
        print("Aluno ficou de EXAME!")
    elif media >= 7:
        print("Aluno APROVADO!")
    
    print("+-------------------------+")

print("+-------------------------+")
print(f"A média total dos alunos foi de: {round(soma_media / 6)}")