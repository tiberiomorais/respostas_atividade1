# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input('informe a nota1'))
nota2 = float(input('informe a nota2'))
nota3 = float(input('informe a nota3'))
nota4 = float(input('informe a nota4'))
notas = [nota1,nota2,nota3, nota4]
media = sum(notas) / len(notas)         # calcula a soma do vetor notas dividido pelo tamanho do vetor

print('A média bimestral é: {}'.format(media))          #usando as chaves representando a função media
