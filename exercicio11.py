print("Exercício 11 (Fibonacci) \n")

num= int(input ("Informe um número: "))
a= 0
b= 1

print("\nSequência de Fibonacci\n")
print(f"{a}",end=", ")
for i in range(1,num):
    c=a+b
    if(i != (num - 1)):
        print(f"{c}",end=", ")
    else: print(f"{c}", end=". ")
    a=b
    b=c 
    

    

