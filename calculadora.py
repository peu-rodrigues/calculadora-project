from typing import Union
import math

Number = Union[int, float]

def somar(a: Number, b: Number) -> Number:
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a: Number, b: Number) -> Number:
    """Retorna a subtração de dois números."""
    return a - b

def multiplicar(a: Number, b: Number) -> Number:
    """Retorna a multiplicação de dois números."""
    return a * b

def dividir(a: Number, b: Number) -> Union[Number, str]:
    """Retorna a divisão de dois números ou mensagem de erro."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero."

def exponenciar(a: Number, b: Number) -> Number:
    """Retorna a potência de a elevado a b."""
    return a ** b

def raiz_quadrada(a: Number) -> Union[Number, str]:
    """Retorna a raiz quadrada de um número ou mensagem de erro."""
    if a < 0:
        return "Erro: número negativo não possui raiz quadrada real."
    return math.sqrt(a)

def main() -> None:
    while True:
        print("\n=== Calculadora Python Profissional ===")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Exponenciar")
        print("6. Raiz Quadrada")
        print("7. Sair")
        escolha = input("Escolha uma operação (1-7): ")

        if escolha == '7':
            print("Encerrando...")
            break

        if escolha not in {'1','2','3','4','5','6'}:
            print("Opção inválida, tente novamente.")
            continue

        try:
            if escolha == '6':
                num1 = float(input("Digite o número: "))
            else:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida, digite números válidos.")
            continue

        if escolha == '1':
            resultado = somar(num1, num2)
        elif escolha == '2':
            resultado = subtrair(num1, num2)
        elif escolha == '3':
            resultado = multiplicar(num1, num2)
        elif escolha == '4':
            resultado = dividir(num1, num2)
        elif escolha == '5':
            resultado = exponenciar(num1, num2)
        elif escolha == '6':
            resultado = raiz_quadrada(num1)

        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
