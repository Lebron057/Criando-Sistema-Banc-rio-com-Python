# deposito | saque | extrato

menu = """
Escolha uma das opções abaixo:
[d] - depósito
[s] - saque
[e] - extrato
[q] - sair
Opção: """


saldo = 1000.00
LIMITE_SAQUE = 500
LIMITE_SAQUES_DIARIO = 3
extrato = ""
numero_saques = 0

while True:
    opcao = input(menu).lower().strip()

    if opcao == "d":
        deposito = float(input("Valor do depósito: R$"))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"

        else:
            print("Valor inválido")

    elif opcao == "s":
        saque = float(input("Valor do saque: R$"))

        if saque > LIMITE_SAQUE:
            print("Valor máximo de saque é de R$500,00")

        elif saque > saldo:
            print("Saldo insulficiente para realizar saque!")

        elif numero_saques >= LIMITE_SAQUES_DIARIO:
            print("Numero máximo de saques atingido")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}"          
            numero_saques += 1

        else:
            print("Valor inválido")

    elif opcao == "e":
        if extrato == "":
            print()
            print("Extrato".center(20, "="))
            print("Não foram realizadas movimentações.\n")

        else:
            print()
            print("Extrato".center(20, "="))
            print(f"{extrato}\n")
        
        print("Saldo".center(20, "="))
        print(f"R${saldo:.2f}\n")
        
    elif opcao == "q":
        break

    else:
        print("Opção inválida, tente novamente")