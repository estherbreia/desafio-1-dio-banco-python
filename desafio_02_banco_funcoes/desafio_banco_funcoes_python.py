menu = """
MENU
Selecione uma opção:
[u] Criar novo usuário
[c] Criar nova conta
[l] Listar contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

def sacar(*, valor, saldo, limite, numero_saques, limites_saques, extrato):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limites_saques

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

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def exibir_extrato(saldo, /, *,extrato):    
    print("\nEXTRATO")
    print("Não foram realizadas mdovimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")


def criar_usuario(usuarios):
    cpf= input("Informe seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nERRO!\nUsuário já cadastrado.")
        return

    nome = input("Informe Seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd/mm/aaaa): " )
    endereco = input("Informe seu endereço (rua, nº - bairro - Cidade/Estado(sigla)):")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\nUsuário criado com sucesso!")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nERRO! \nUsuário não encontrado.")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print(linha)
    

def main():
    
    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1
    

    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)



        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                valor=valor,
                limite=limite, 
                saldo=saldo,
                numero_saques=numero_saques, 
                limites_saques=LIMITE_SAQUES, 
                extrato=extrato
            )
        

        elif opcao == "e":
            exibir_extrato(
                saldo, 
                extrato=extrato
            )
        
        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao =="c":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1


        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()