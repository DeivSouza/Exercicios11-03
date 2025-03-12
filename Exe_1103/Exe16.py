#16 Faça um programa que calcula a tabuada dos números 2 a 9;

tabuada = 2

for n in range (2, 10):
    for i in range (11):
        print(f"{tabuada} x {i} = {tabuada * i}")
    print("--------------------------------------")
    tabuada += 1