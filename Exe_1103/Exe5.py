#5 Faça um programa que recebe um número em Pés, faça as conversões a seguir e mostre os resultados.
#Polegadas;
#Jardas;
#Milhas;
#Sabe –se que:
#1 Pé = 12 polegadas;
#1 Jarda = 3 Pés;
#1 Milha = 1.760 Jarda;

pe = float(input("Informe a metragem em PÉS: "))

polegada = pe * 12
jardas = pe / 3
milha = jardas / 1760

print(f"{pe} PÉS em polegadas, são: {polegada}")
print(f"{pe} PÉS em jardas, são {jardas}")
print(f"{pe} PÉS em milha, são: {round(milha, 4)}")