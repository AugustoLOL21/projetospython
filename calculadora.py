# Função para adicionar dois números
def adicionar(x, y):
    return x + y

# Função para subtrair o segundo número do primeiro
def subtrair(x, y):
    return x - y

# Função para multiplicar dois números
def multiplicar(x, y):
    return x * y

# Função para dividir o primeiro número pelo segundo
def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida"
    else:
        return x / y


def main():
    while True:
        # Exibindo o menu de opções
        print("\nCalculadora Digital")
        print("Selecione a operação desejada:")
        print("1. Adicionar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        # Capturando a escolha do usuário
        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        # Verificando se a escolha é sair
        if escolha == '5':
            print("Obrigado por usar a calculadora. Até logo!")
            break

        # Verificando se a escolha é válida
        if escolha in ['1', '2', '3', '4']:
            # Capturando os números para a operação
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite números válidos.")
                continue

            # Executando a operação correspondente
            if escolha == '1':
                print(f"Resultado: {num1} + {num2} = {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                resultado = dividir(num1, num2)
                if resultado == "Erro: Divisão por zero não é permitida":
                    print(resultado)
                else:
                    print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Escolha inválida. Por favor, selecione uma opção válida.")
if __name__ == "__main__":
    main()


# Funções para operações matemáticas
def adicionar(x, y):
    return x + y


def subtrair(x, y):
    return x - y


def multiplicar(x, y):
    return x * y


def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida"
    else:
        return x / y


# Função principal que executa o menu e as operações
def main():
    while True:
        print("\nCalculadora Digital")
        print("Selecione a operação desejada:")
        print("1. Adicionar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha == '5':
            print("Obrigado por usar a calculadora. Até logo!")
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite números válidos.")
                continue

            if escolha == '1':
                print(f"Resultado: {num1} + {num2} = {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                resultado = dividir(num1, num2)
                if resultado == "Erro: Divisão por zero não é permitida":
                    print(resultado)
                else:
                    print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Escolha inválida. Por favor, selecione uma opção válida.")


# Executando o programa principal
if __name__ == "__main__":
    main()
