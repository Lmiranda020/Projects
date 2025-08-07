#deposito, saque e extato

print('Olá bem vindo(a) ao banco da DIO')

nome = input("Digite o seu nome: ")

print(f'Bem vindo(a)! {nome}. Digite uma das opções abaixo para prosseguir'
      )

opções = """
    [1] - Deposito
    [2] - Saque
    [3] - Extrato
    [4] - Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



while True:

    print(opções)
    opção_escolhida = input('Digite a sua opção: ')

    if opção_escolhida == "1":
        
        valor_deposito = float(input("Informe o valor do depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n" # aqui ele vai juntando com quebra de linha, para apecer um embaixo do outro

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opção_escolhida == "2":
    
        valor_saque = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor_saque > saldo

        excedeu_limite = valor_saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opção_escolhida == "3":
    
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")


    elif opção_escolhida == "4":
        print("Vocês está deixando o banco da DIO, volte sempre! Obrigada ")
        break

    else: print("Opção invalida, por digite uma das opções a seguir: ")