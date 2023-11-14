from meus_modulos.numeros.soma import somarNumeros
from meus_modulos.numeros.subtracao import subtrairNumero
from meus_modulos.numeros.divisao import dividirNumero
from meus_modulos.numeros.multiplicacao import multiplicarNumero
def menu():
    while True:
        print('1 - somar')
        print('2 - subtração')
        print('3 divisão')
        print('4 - multriplicação')
        opcao = input('Selecione uma opçao: ')
        if opcao == '1':
            num1 = float(input('Digite o primeiro valor: '))
            num2 = float(input('Digite o segundo valor: '))
            print(f'Resultado: {somarNumeros(num1, num2)}')
        elif opcao == '2':
            num1 = float(input('Digite o primeiro valor: '))
            num2 = float(input('Digite o segundo valo: '))
            print(f'Resultado: {subtrairNumero(num1, num2)}')
        elif opcao == '3':
            num1 = float(input('Digite o primeiro valor: '))
            num2 = float(input('Digite o segundo valo: '))
            print(f'Resultado: {dividirNumero(num1, num2)}')
        elif opcao == '4':
            num1 = float(input('Digite o primeiro valor: '))
            num2 = float(input('Digite o segundo valo: '))
            print(f'Resultado: {multiplicarNumero(num1, num2)}')
menu()






