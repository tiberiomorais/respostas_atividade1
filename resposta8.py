# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

sal_hora = float(input('Informe quanto você ganha por hora:'))
horas_trab_mes = float(input('Informe o numero de horas trabalhadas nesse mês'))

salario = sal_hora * horas_trab_mes



def formatar(salario, cifrao = 'R$'):   #funcao que recebe o salario/h e atribui cifrao=R$
      return f'{cifrao}{salario:.2f}'.replace('.',',')   #add R$ ao lado do valor e substitui o ponto pela virgula

print('O salário mensal é:',formatar(salario))