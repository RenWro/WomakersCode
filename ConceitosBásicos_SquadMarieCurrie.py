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


'''
#Exercício 3

def converter_distancias():
    # Pede ao usuário a quantidade de quilômetros
    quilometros = float(input("Digite a quantidade de quilômetros: "))

    # Converte
    metros = quilometros * 1000
    centimetros = quilometros * 100000
    milimetros = quilometros * 1000000

    print(f"{quilometros} km é igual a {metros} metros.")
    print(f"{quilometros} km é igual a {centimetros} centímetros.")
    print(f"{quilometros} km é igual a {milimetros} milímetros.")


converter_distancias()
'''

'''
#Exercíio 4

def calcular_consumo_medio():
    # Pede do usuário os litros consumidos e a distância percorrida
    litros_consumidos = float(input("Digite a quantidade de litros de combustível consumidos: "))
    distancia_percorrida = float(input("Digite a distância percorrida em quilômetros: "))

    # Calcula o consumo médio
    consumo_medio = distancia_percorrida / litros_consumidos

    print(f"O consumo médio é {consumo_medio:.2f} km/l.")


calcular_consumo_medio()
'''

'''
# Exercicio 5

def calcular_salario_liquido():
    
    salario_bruto = float(input("Digite o salário bruto: R$ "))

    # Define as alíquotas e limites
    aliquotas = [(0, 1903.98, 0),
                 (1903.99, 2826.65, 0.075),
                 (2826.66, 3751.05, 0.15),
                 (3751.06, 4664.68, 0.225),
                 (4664.68, float('inf'), 0.275)]

    # Calcula o IR
    imposto_de_renda = 0
    for faixa in aliquotas:
        if salario_bruto > faixa[0] and salario_bruto <= faixa[1]:
            imposto_de_renda = (salario_bruto - faixa[0]) * faixa[2]
            break

    # Calcula o salário líquido
    salario_liquido = salario_bruto - imposto_de_renda

    print(f"Salário bruto: R$ {salario_bruto:.2f}")
    print(f"Imposto de renda: R$ {imposto_de_renda:.2f}")
    print(f"Salário líquido: R$ {salario_liquido:.2f}")

calcular_salario_liquido()
'''

'''

# Exercicio 6

def calcular_tempo_viagem():
    distancia = float(input("Digite a distância da viagem em km: "))

    velocidade_aviao = 600
    velocidade_carro = 100
    velocidade_onibus = 80

    # Função para converter horas em horas e minutos
    def converter_para_horas_e_minutos(tempo_em_horas):
        horas = int(tempo_em_horas)
        minutos = int((tempo_em_horas - horas) * 60)
        return (horas, minutos)

    # Converte para horas e minutos
    horas_aviao, minutos_aviao = converter_para_horas_e_minutos(distancia / velocidade_aviao)
    horas_carro, minutos_carro = converter_para_horas_e_minutos(distancia / velocidade_carro)
    horas_onibus, minutos_onibus = converter_para_horas_e_minutos(distancia / velocidade_onibus)

    # Imprime o tempo de viagem para cada meio de transporte em horas e minutos
    print(f"Tempo de viagem de avião: {horas_aviao} horas e {minutos_aviao} minutos")
    print(f"Tempo de viagem de carro: {horas_carro} horas e {minutos_carro} minutos")
    print(f"Tempo de viagem de ônibus: {horas_onibus} horas e {minutos_onibus} minutos")

calcular_tempo_viagem()

'''


'''
# Exercicio 7

def calcular_imc():
    # Solicita o peso e a altura
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros (exemplo: 1.68): "))

    # Calcula o IMC
    imc = peso / (altura ** 2)

    print(f"Seu Índice de Massa Corporal (IMC) é: {imc:.2f}")

calcular_imc()
'''

'''
# Exercicio 8

def calcular_salario_mensal():

    valor_hora = float(input("Quanto você ganha por hora? "))
    horas_mes = float(input("Quantas horas você trabalhou no mês? "))

    # Calcula o salário total
    salario_total = valor_hora * horas_mes

    print(f"O total do seu salário no mês é: R$ {salario_total:.2f}")


calcular_salario_mensal()
'''

'''
# Exercicio 9



def calcular_calorias_queimadas():
    horas_semana = float(input("Quantas horas por semana você se exercita? "))

    # Converte horas em minutos
    minutos_semana = horas_semana * 60

    # Considera uma média de 5 calorias por minuto de exercício
    calorias_por_minuto = 5

    # Calcula o total de calorias queimadas por semana
    calorias_semana = minutos_semana * calorias_por_minuto

    # Calcula o total de calorias queimadas por mês (considera 4 semanas no mês)
    calorias_mes = calorias_semana * 4

    # Imprime o total de calorias no mês
    print(f"Total de calorias queimadas no mês: {calorias_mes:.0f} calorias")


calcular_calorias_queimadas()
'''


# Exercicio 10


#Exercício 10

def mensagem_amigavel():
    # Variáveis fornecidas
    nome_dj = input("Qual é o nome da DJ? ")
    anos_tocando = input("Há quantos anos você toca? ")
    estado_origem = input("De qual estado você é? ")
    ritmo_musical = input("Qual ritmo musical você toca? ")

    # Mensagem amigável utilizando as variáveis
    mensagem = (
        f"Olá DJ {nome_dj}, prazer te conhecer. "
        f"Soube que você toca há {anos_tocando} anos, "
        f"vem do estado de {estado_origem} e é especialista em {ritmo_musical}. "
        "Estou aqui para ajudar no que precisar no universo musical!"
    )

    print(mensagem)


mensagem_amigavel()



