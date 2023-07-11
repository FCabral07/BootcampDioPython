# Definindo o menu
menu = """
1- Depositar
2- Sacar
3- Extrato
4- Saldo
5- Sair
"""

# Definindo variáveis a serem usadas
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3
condicao = 100

# Criando as lógicas dos menus
def depositar():
    global saldo, extrato
    valor = float(input('\nDigite o valor do depósito: '))
    if valor > 0:
        saldo += valor
        extrato += f'\nDéposito de R${valor:.2f}'
        return f'Depósito efetuado com sucesso.\nSaldo de: {saldo:.2f}'
    else:
        return f'Depósito não efetuado, por favor selecione um valor válido.\n'

def sacar():
    global saldo, numero_saque, extrato
    valor = float(input('\nInforme o valor do saque: '))
    
    saldo_menor = saldo < valor
    valor_maior = valor > limite
    saques_excedidos = numero_saque >= LIMITE_SAQUE

    if saldo_menor:
        return 'Saldo insuficiente.'
    elif valor_maior:
        return 'O valor ultrapassa seu limite de saque diário.'
    elif saques_excedidos:
        return 'Você já fez todos os saques permitidos no dia de hoje.'
    else:
        saldo -= valor
        extrato += f'\nSaque de R${valor:.2f}'
        numero_saque += 1
        return f'Saque efetuado com sucesso.\nSaldo de: {saldo:.2f}'

def extrato_cliente():
    global extrato
    return f'---------------EXTRATO:---------------\n{extrato}\n--------------------------------------'

def saldo_cliente():
    global saldo
    return f'Saldo: R${saldo:.2f}'

def sair():
    return 'Obrigado pela preferência.\n'

# Criando um dict onde armazena as opções e operações do menu
switcher_menu = {
    1: depositar,
    2: sacar,
    3: extrato_cliente,
    4: saldo_cliente,
    5: sair
}

# Parte 'main' do programa, onde acontece tudo
while condicao>0:
    print(menu)
    escolha_menu = int(input("Escolha a opção desejada: "))

    resultado = switcher_menu.get(escolha_menu)
    if resultado:
        print(f'\n{resultado()}')
    else:
        print('Opção inexistente, selecione outra opção.')

    if escolha_menu == 5:
        condicao = 0