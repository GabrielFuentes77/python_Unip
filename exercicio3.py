#Função para verificar se um numero é par ou impar
def testePar(n1):
    teste = False
    if(n1%2==0):
        teste = True
    return teste
        
num = int(input("Informe um número: "))

verifica = testePar(num)

if(verifica == True):
    print(f"O número {num} é par!")
else: 
    print(f"O número {num} é impar!")

