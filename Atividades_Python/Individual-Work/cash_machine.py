def menu():
    print('\033[1;33m=' * 35)
    print('{:^40}'.format('\033[1;33mBANCO LUCAS'))
    print('\033[1;33m=' * 35)
    
def carregamento(n100, n50, n20, n10, n5):
    s = 0
    deposito = n100 + n50 + n20 + n10 + n5
    print(f'\n\033[1;36mVocê depositou: R${deposito},00\n')
    s += n100 + n50 + n20 + n10 + n5 
    return s

def valorNaConta():
    n100 = int(input('\033[1;95mQuantas notas de 100: ')) * 100
    n50 = int(input('\033[1;95mQuantas notas de 50: ')) * 50
    n20 = int(input('\033[1;95mQuantas notas de 20: ')) * 20
    n10 = int(input('\033[1;95mQuantas notas de 10: ')) * 10
    n5 = int(input('\033[1;95mQuantas notas de 5: ')) * 5
    conta = carregamento(n100, n50, n20, n10, n5)
    return conta 

def saque():
    valor = int(input('\nDigite valor do saque: '))
    valor_saque = 0
    valor_saque += valor
    return valor_saque

saldo = 0 

caixaAberto = True
while caixaAberto:
    menu()
    opcao = int(input('\033[1;94m\n1. Carregar Caixa Eletrônico. \n2. Consultar saldo. \n3. Sacar dinheiro. \n4. Sair.\n\n'))
    if opcao == 1:
        saldo += valorNaConta()
    elif opcao == 2:
        if saldo > 0:
            print(f'\n\033[1;90mSeu saldo é: R$ {saldo},00\n')
        else:
            print(f'\033[1;91m>>>Conta vazia<<<')
    elif opcao == 3:
        valorSaque = saque()
        if saldo >= valorSaque:
            total = valorSaque
            ced = 100
            totalced = 0
            while True:
                if total >= ced:
                    total -= ced
                    totalced += 1
                else:
                    if totalced > 0:
                        print(f'\033[1;37mTotal de {totalced} de cedulas de {ced}')
                    if ced == 100:
                        ced = 50
                    elif ced == 50:
                        ced = 20
                    elif ced == 20:
                        ced = 10
                    elif ced == 10:
                        ced = 5
                    totalced = 0
                    if total == 0:
                        print('\033[1;32m=' * 35)
                        print(f'\033[1;32mSaque no valor total de: R$ {valorSaque},00')
                        print('\033[1;32m=' * 35)
                        saldo -= valorSaque 
                        break
                    elif total < 5:
                        print('\033[1;91m=' * 113)
                        print('{:^113}'.format('\033[1;91mOPERAÇÃO CANCELADA!'))
                        print('{:^113}'.format('\033[1;91m>>>As cédulas disponíveis neste caixa não permitem concluir esta transação - [Saque apenas com multiplos de 5]<<<'))
                        print('\033[1;91m=' * 113)
                        break
        else:
            print('\n\033[1;31m>>>[Saldo insuficiente]<<<')
    if opcao == 4:
        print('\n>>>[Obrigado - Volte sempre!]<<<\n')
        caixaAberto = False