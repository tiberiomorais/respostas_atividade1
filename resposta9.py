# 9. Faça um Programa que peça a temperatura em graus Farenheit,
#    transforme e mostre a temperatura em graus Celsius

temp_far = float(input('Informe a temperatura em Farenheit'))
temp_cel = 5 * (temp_far - 32) / 9



def formatar_cel(temp_cel, cel = 'ºC'):
    return f'{temp_cel}{cel}'

def formatar_far(temp_far, far = 'ºF'):
    return f'{temp_far}{far}'


print(formatar_far(temp_far), 'corresponde a',formatar_cel(temp_cel))