def fibonacci(n: int):
    if(n<=2):
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

def main():
    n = int(input("Ingrese un número a calcular: "))
    print(fibonacci(n))

if __name__ == "__main__":
    main()