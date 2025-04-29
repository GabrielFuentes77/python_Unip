def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

def main():
    n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))
    if n <= 0:
        print("Por favor, digite um número maior que zero.")
    else:
        print("Sequência de Fibonacci:")
        fibonacci(n)

if __name__ == "__main__":
    main()
    

