"""
Metodo que que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida.
Autor: João Gilberto Canal Favaro
Data:  08/09/2022 15:05
"""


#Declaração da Variavel
opção = 0
while opção !=5:
n1= int(input ('Primeiro Valor: '))
n2= int(input ('Segundo Valor: '))

#Criar o Menu
print('''[ 1 ] Somar
[ 2 ] Subtração
[ 3 ] Multiplicar
[ 4 ] Dividir
[ 5 ] Ir Embora''')

opção = str(input('Oque você deseja?: '))

 if opção == 1
    soma=n1+n2
    print('A soma entre {} e {} é {} '.format(n1, n2, soma))

 elif opção == 2
 soma=n1-n2
    print('A subtração entre {} e {} é {} '.format(n1, n2, subtração))

 elif opção == 3
 soma=n1*n2
    print('A multiplicação entre {} e {} é {} '.format(n1, n2, produto))

 elif opção == 4
  soma=n1/n2
    print('A Divisão entre {} e {} é {} '.format(n1, n2, divisão))

 elif opção == 5
  print('Finalizando')
 else :
     print('Erro')
     print(=-= * 10)
            

