# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math                  #importando biblioteca matemática
raio = float(input('Informe o raio do circulo:'))
area = math.pi * raio ** 2  #funcao math.pipega o valor de pi
print('a área do circulo de raio ',raio, 'mede {:.2f}'.format(area))     #novamente utilizo {:.2f} para representrar com 2 casas decimais a func area
                            #tambem poderia ser round(area,2)
