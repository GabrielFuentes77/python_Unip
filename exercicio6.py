print("Exercicio 6 (Tabuada)\n")

num = int(input("Informe um número de 1 a 10: "))
while(num < 0 or num > 10):
    num = int(input("número fora dos parametros, informe outro número: "))

print(f"\nTabuada do número {num}\n")


for i in range(1,11):
    print(f"{num} x {i} = {(num*i)}" )
    