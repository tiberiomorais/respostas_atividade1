# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input('Informe o lado do quadrado'))
area_quadrado = lado ** 2
dobro_area = area_quadrado * 2
print('O dobro da area de um quadrado de lado {}'.format(lado),', area {}'.format(area_quadrado), 'é:{}'.format(dobro_area))