# Definindo o menu
menu = """
1- Criar Usuário
2- Criar Conta
3- Depositar
4- Sacar
5- Extrato Cliente
6- Saldo Cliente
7- Listar Contas
8- Sair
}
"""

# Definindo variáveis a serem usadas
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3
usuarios = {}
contas = {}
AGENCIA = 1
numero_conta = 1000
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

def criar_usuario():
    cpf = input("Informe o CPF só com os números: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        return 'Já existe um usuário com esse CPF.'
    
    nome = input("Informe o nome completo: ")
    data_nasc = input('Informe a data de nascimento separado por barras dd/mm/aaaa: ')
    usuarios[cpf] = {"nome": nome, "data_nasc": data_nasc, "cpf": cpf}
    return 'Usuário criado com sucesso.'

def filtrar_usuario(cpf, usuarios):
    return usuarios.get(cpf)

def criar_conta():
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        global numero_conta
        numero_conta += 1
        contas[numero_conta] = ({'agencia': AGENCIA, 'conta': numero_conta, 'usuario': usuarios[cpf]})
        return 'Conta criada com sucesso'

def listar_contas():
    global contas, numero_conta
    clientes = ''
    if contas:
        for numero_conta, conta in contas.items():
            clientes += f'Agência: {conta["agencia"]}, Conta: {numero_conta}, Usuário: {conta["usuario"]["nome"]}\n'
        return clientes
    else:
        return 'Nenhuma conta encontrada.'

def sair():
    return 'Obrigado pela preferência.\n'

# Criando um dict onde armazena as opções e operações do menu
switcher_menu = {
    1: criar_usuario,
    2: criar_conta,
    3: depositar,
    4: sacar,
    5: extrato_cliente,
    6: saldo_cliente,
    7: listar_contas,
    8: sair
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

    if escolha_menu == 8:
        condicao = 0