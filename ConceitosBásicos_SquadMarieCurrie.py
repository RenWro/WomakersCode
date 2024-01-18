'''
#Exercício 1

def main():
    # Solicita números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realiza operações
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2 if num2 != 0 else "Divisão por zero não é permitida"

    # Exibe resultados
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")

main()
'''

'''
#Exercício 2
from datetime import datetime


def calcular_idade():
    # Pega o ano e o mês atuais
    ano_atual = datetime.now().year
    mes_atual = datetime.now().month

    # Pede para informar o ano e o mês de nascimento
    ano_nascimento = int(input("Informe o ano de nascimento: "))
    mes_nascimento = int(input("Informe o mês de nascimento (1-12): "))

    # Calcula a idade
    idade = ano_atual - ano_nascimento
    # Subtrai 1 da idade se o usuário ainda não fez aniversário
    if mes_atual < mes_nascimento:
        idade -= 1

    # Imprime a idade
    print(f"Sua idade atual é: {idade} anos")


calcular_idade()
'''
