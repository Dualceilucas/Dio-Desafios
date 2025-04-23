menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:  # Verifica se o limite de saques foi atingido
            print("Operação falhou! Você já realizou o limite máximo de saques do dia.")
        else:
            while True:  # Loop para garantir que o valor do saque seja válido
                valor = float(input("Informe o valor do saque: "))
            
                if valor <= 0:  # Barrando valores negativos ou iguais a zero
                    print("O valor informado deve ser positivo. Tente novamente.")
                    continue  # Volta ao início do loop para pedir novamente
            
                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite
            
                if excedeu_saldo:
                    print("Operação falhou! Você não tem saldo suficiente. Tente novamente.")
            
                elif excedeu_limite:
                    print("Operação falhou! O valor do saque excede o limite. Tente novamente.")
            
                else:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    numero_saques += 1
                    print("Saque realizado com sucesso!")
                    break  # Sai do loop após realizar um saque válido
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")