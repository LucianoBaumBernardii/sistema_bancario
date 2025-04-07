saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3


def limpar_tela():
    return 'cls'

limpar_tela()

while True :
    print('\nBem vindo ao atendimento do banco BAHIA \n\n Escolha a opção de atendimento:\n')
    opcao = input('[1] Saque            [2] Depósitos\n[3] Extrato          [4] Outras Opções\n\n\n')

    if opcao == '2' :
        print("Qual valor deseja depositar? ")
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0 :
            saldo += valor
            extrato += f'Depósito: R$ {valor}'
            print(extrato)
            print(f'O saldo atualizado é de R$: {saldo}')
        else:
            print('Falha na operação, o valor informado é inválido.')

    elif opcao == '1' :
        print("Qual valor deseja sacar? ")
        valor = float(input('Informe o valor do saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(extrato)
            print(f'Saldo atualizado R$: {saldo}')

        else:
            print('Falha na operação, o valor informado é inválido.')

    elif opcao == '3':        
        print('\n================== EXTRATO ===================')
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo}')
        print('================================================')


    elif opcao == '4':
        print('Procure nossos canais de atendimento ou fale com seu gerente.')
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.") 