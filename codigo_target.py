import json
'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre
será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, ele calcule
 a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
  pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode
 ser previamente definido no código;
'''


def fibbo(number):
    fA = 1
    fB = 0
    fC = 0
    while fC <= number:
        if number == 0:
            return True
        else:
            fC = fA + fB
            fB = fA
            fA = fC

        if fC == number:
            return True

    return False


while True:
    try:
        entry = int(input('Digite um número inteiro: '))
        if fibbo(entry):
            print(f'O número {entry} pertence a sequencia Fibonacci.')
        else:
            print(f'O número {entry} não pertence à sequencia Fibonacci.')
        break
    except (TypeError, ValueError):
        print('Digite somente números inteiros !!!')


'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média
mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados.
Estes dias devem ser ignorados no cálculo da média;
'''


def dataJson(file):
    with open(file, 'r') as content:
        data = json.load(content)
    return data


def recoveryData(data):
    dataValid = []

    for i in data:
        for c, v in i.items():
            if c == 'valor' and v > 0:
                dataValid.append(v)

    return dataValid


def average(data=[]):
    data = sum(data) / len(data)
    return round(data, 2)


def minimum(data=[]):
    data = min(data)
    return round(data, 2)


def maximum(data=[]):
    data = max(data)
    return round(data, 2)


def daysAboveAverage(averageValue, data=[]):
    numberOfDays = 0
    for i in data:
        if i > averageValue:
            numberOfDays += 1
    return numberOfDays


data = recoveryData(dataJson('dados.json'))

print(f'O menor valor de faturamento encontrado no período: R$ {minimum(data)}')
print(f'O maior valor de faturamento encontrado no período: R$ {maximum(data)}')
print(f'Número de dias em que o valor do faturamento foi maior que a média mensal:'
      f' {daysAboveAverage(average(data), data)}')


'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação
que cada estado teve dentro do valor total mensal da distribuidora.
'''

data = [
    {'estado': 'SP', 'valor': 67836.43},
    {'estado': 'RJ', 'valor': 36678.66},
    {'estado': 'MG', 'valor': 29229.88},
    {'estado': 'ES', 'valor': 27165.48},
    {'estado': 'OUTROS', 'valor': 19849.53}
]


def totalSum(data=[]):
    tSum = 0
    for i in data:
        for k, v in i.items():
            if k == 'valor':
                tSum += v
    return tSum


def percentByState(state=str, data=[]):
    state = state.upper()
    for i in data:
        for k, v in i.items():
            if v == state:
                p = i['valor']
                percent = (p * 100) / totalSum(data)
                return round(percent, 2)


def printAllStates(data=[]):
    for i in data:
        for k, v in i.items():
            if k == 'estado':
                print(f'O percentual do estado {v} foi de: {percentByState(v, data)}%')


printAllStates(data)


'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência
 ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

myString = input('Digite algo: ')

myStringInvert = []
for i in myString[::-1]:
    myStringInvert.append(i)

myStringInvertStr = ''.join(myStringInvert)

print(myStringInvertStr)
