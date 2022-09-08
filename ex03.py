"""
Metodo que receba como parâmetros preenchidos pelo usuário, os valores dos lados de um triângulo e classifique como "Equilátero, Escaleno ou Isósceles".
Autor: João Gilberto Canal Favaro
Data:  08/09/2022 14:39
"""

#Declaração da Variavel
r1 = float(input('Primeiro Seguimento: '))
r2 = float(input('Segundo Seguimento: '))
r3 = float(input('Terceiro Seguimento: '))

#Definido od triangulos
 if r1 > r2 + r3 and r2 > r1 + r3 and r3 < r1 + r2 :
     print('Os seguimento acima podem formar um triangulo ', end="")
     if r1 == r2 == r3:
         print('Equilátero !')
     if r1 != r2 != r3:
         print('Escaleno !')
     else
     print('isósceles !')

     else:
         print('Os seguimento acima não podem formar um triangulo ')
         
         
         
