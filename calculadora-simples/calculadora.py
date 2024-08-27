def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    else:
        return a / b 
    
def menu():
        try:
            print("Calculadora Simples")
            print("--------------------")
            print("1. Adição")
            print("2. Subtração")
            print("3. Multiplicação")
            print("4. Divisão")
            print("5. Sair")
        except ValueError:
                print("Digite apenas números")

def obter_valores():
    while True:
        try:
            a = float(input("Digite o primeiro valor: "))
            b = float(input("Digite o segundo valor: "))
            return a, b
        except ValueError:
            print("Erro, você deve digitar um número!")


def realizar_operacao(opcao, a, b):
    if opcao == 1:
        return soma(a, b)
    elif opcao == 2:
        return subtracao(a, b)
    elif opcao == 3:
        return multiplicacao(a, b)
    elif opcao == 4:
        return divisao(a, b)
    else:
        return "Opção inválida"
    
    
def exibir_resultado(resultado):
    print("Resultado: ", resultado)


def main():
    while True:
        menu()
        while True:
            opcao = input("Digite a opção: ")
            if opcao.isdigit():
                opcao = int(opcao)
                if opcao < 1 or opcao > 5:
                    print("Opção inválida. Digite um número entre 1 e 5!")
                else:
                    break
            else:
                print("Erro:  Digite apenas números")

            if opcao == 5:
                print("Saindo do programa...")
                break

        a, b = obter_valores()
        resultado = realizar_operacao(opcao, a, b)
        exibir_resultado(resultado)


if __name__ == "__main__":
    main()