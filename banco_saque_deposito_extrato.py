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
        valor = int(input("Informe valor p/ depósito: "))
        if valor > 0:
           saldo += valor
        
        
        else:
            print("Valor Invalido! Operação falhou. ")

    
    elif opcao == "s":
        valor = float(input("Digite o valor do Saque: "))

        excedeu_saldo = valor > saldo
       
        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
       
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
        
    elif opcao == "e":
        print(f"Seu saldo é de R$ {saldo:2}")

   
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")