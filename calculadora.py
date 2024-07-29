

def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        raise ValueError("Não é possível dividir por zero.")
    return x / y

def main():
    print("Operações disponíveis:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        escolha = input("Escolha uma operação (1/2/3/4) ou 'sair' para terminar: ").strip().lower()

        if escolha == 'sair':
            print("Encerrando a calculadora. Até mais!")
            break
        
        if escolha not in ['1', '2', '3', '4']:
            print("Opção inválida. Tente novamente.")
            continue
        
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"{num1} + {num2} = {adicionar(num1, num2)}")

            elif escolha == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")

            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

            elif escolha == '4':
                try:
                    resultado = dividir(num1, num2)
                    print(f"{num1} / {num2} = {resultado}")
                except ValueError as e:
                    print(e)
        
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")

if __name__ == "__main__":
    main()

