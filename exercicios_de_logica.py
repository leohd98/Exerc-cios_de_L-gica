# Exercício 1 ----------------------------------
# Faça um algoritmo que leia os valores de A, B e C e em seguida
# imprima na tela a soma entre A e B, e mostre se a soma é menor que C.

# V1 = int(input('Valor 1: '))
# V2 = int(input('Valor 2: '))
# V3 = int(input('Valor 3: '))
# x = V1 + V2
# if x > V3:
#     print(f'A soma dos primeiros 2 valores ({x}) é maior do que o terceiro valor ({V3})')
# elif x == V3:
#     print(f'A soma dos primeiros 2 valores ({x}) é igual ao terceiro valor ({V3})')
# else:
#     print(f'A soma dos primeiros 2 valores ({x}) é menor do que o terceiro valor ({V3})')

# ----------------------------------------------

# Exercício 2 ----------------------------------
# Encontre o maior número em uma lista: Escreva um algoritmo para encontrar o maior número em uma lista de valores.

# lista = [1, 4, 5, 9, 2, 5, 6, 0, 12, 1, 55]
# valor = lista[0]
# for numero in lista:
#     if numero > valor:
#         valor = numero
# print(f'O maior número da lista é {valor}')

# ----------------------------------------------

# Exercício 3 ----------------------------------
# Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar
# positivo ou negativo.

# numero = int(input('Digite um número: '))
# par_ou_impar = ''
# negativo_ou_positivo = ''
# if numero % 2 == 0:
#     par_ou_impar = 'Par'
#     if numero < 0:
#         negativo_ou_positivo = 'Negativo'
#     else:
#         negativo_ou_positivo = 'Positivo'
# else:
#     par_ou_impar = 'Ímpar'
#     if numero < 0:
#         negativo_ou_positivo = 'Negativo'
#     else:
#         negativo_ou_positivo = 'Positivo'
# print(f'{numero} é um valor {negativo_ou_positivo} e é um número {par_ou_impar}.')

# ----------------------------------------------

# Exercício 4 ----------------------------------
# Verifique se um número é primo: Crie um programa que determine se um número é primo ou não.

while True:
    numero = int(input('Escolha um número: '))
    if numero < 2:
        print(f'{numero} não é um número primo.')
        print()
    elif numero == 2:
        print(f'{numero} é um número primo, e o único valor primo que é par.')
        print()
    elif numero % 2 == 0:
        print(f'{numero} não é primo, 2 é o único número primo que é par.')
        print()
    else:
        for valor in range(3, numero + 2, 2):
            if numero % valor == 0 and valor == numero:
                print(f'{numero} é um número primo.')
                print()
                break
            elif numero % valor == 0 and valor != numero:
                print(f'{numero} não é um número primo.')
                print()
                break

# ----------------------------------------------
