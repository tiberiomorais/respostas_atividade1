# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.



temp_celsius = float(input('Informe a temperatura em Celsius'))

temp_farenheit = (9 * temp_celsius + 160)/5

def formatar_celsius(temp_celsius, cel ='ºC'):
    return f'{temp_celsius}{cel}'

def formatar_farenheit(temp_farenheit, far = 'ºF'):
    return f'{temp_farenheit}{far}'

print(formatar_celsius(temp_celsius), 'corresponde a:', formatar_farenheit(temp_farenheit))


