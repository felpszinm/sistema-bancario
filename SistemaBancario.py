
from datetime import datetime, timedelta
from time import sleep

menu = """

    \tInicio

    [S] Sacar
    [D] Depositar
    [E] Extrato
    [F] Sair

    => """

def sacar(saldo, saque):                   # Função de sacar o dinheiro. 
    if saldo < saque:        # Se saldo da conta for menor que o valor pedido, aparece a mensagem de erro e retorna a função.
        print('Você não tem saldo suficiente para esse valor')
        return saldo
    
    elif saque < 0:          # Se saque for menor que 0, saque é invalidado e retorna a função.
        print('Saque inválido! Digite novamente o valor: R$ ')
        return saldo
    
    elif saque > 500:               # Se valor for maior que 500 reais do limite, aparece a mensagem de erro e retorna a função.
        print('Limite insuficiente... Seu limite é de R$ 500,00')
        return saldo
    
    elif saldo >= saque and saque < 500: # Se SALDO for igual ou maior e VALOR for menor que 500, saldo vai ser subtraido por valor.
        saldo -= saque
        return saldo # Retorna o saldo atualizado.
    
def depositar(saldo, deposito):
    
    if deposito < 0:    # Se depósito for menor que 0, depósito é invalidado e retorna a função.
        print('Deposito inválido! Digite novamente o valor: R$')
        return saldo
    
    else:
        saldo += deposito
        return saldo    # Retorna o saldo atualizado.
    
def transacoes(limite):
    data = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    limite += 1

    if limite == 3:     # Se as transações (depositos/saques) chegarem a 10, o programa informará a mensagem de limite de transações atingido.
            print(f'Limite de dez transações diárias atingidas da data {data.strftime("%d-%m-%y")}')
            print(f'Transações liberadas a partir da data {(data + timedelta(days=1)).strftime("%d-%m-%y %H:%M")}')
            return False
    return limite
            
        
    

    
saldo = 1000        # Saldo da conta.
limite = 500        # Limite para sacar.
extrato_saque = [] # Lista aonde os saques feitos vão ser cadastrados.
extrato_deposito = [] # Lista aonde os depositos feitos vão ser cadastrados.
numero_saque = 0 
horario_saque = []
horario_deposito = []   
LIMITE_SAQUE = 3
limite_transacoes = 0
data_transacao_saque = []
data_transacao_deposito = []


while True:
    opcao_menu = input(menu).upper()
    
    if opcao_menu == 'F':   # Se for escolhido a opção de sair, ele ira finalizar o while.
        print('Saindo do programa...')
        break
        
    while True:
    
        if opcao_menu == 'S':       # Se escolhido a opção SACAR, é mostrado um input para o usuario sacar o valor.
            if numero_saque == LIMITE_SAQUE:    # Se numero de saque for igual a Limite de saques, aparece uma mensagem de "Limite atingido" e volta para o inicio
                print('Limite de saques atingido!')
                break
            
            data_transacao_saque.append(datetime.now())
            
            limite_transacoes = transacoes(limite_transacoes) # Atualiza o valor de limite_transacoes (Pelo saque)
            if limite_transacoes is False:  # Se a variavel for False (Atribuida na def), o programa para
                break
            
            valor_de_saque = float(input('Digite o valor de saque: R$'))   
            novo_saldo = sacar(saldo, valor_de_saque) # A função retorna valor de saque, e a variavel novo_saldo, atualiza o saldo anterior
            
            if novo_saldo != saldo: # Se o saldo foi alterado, o saque foi bem-sucedido
                saldo = novo_saldo
                print(f'Saldo atualizado no valor de R$ {saldo}')
                numero_saque += 1
                extrato_saque.append(valor_de_saque) # Adiciono o valor de saque para ser contabilizado no extrato.
                break
        
        elif opcao_menu == 'D':     # Se escolhido opção DEPOSITAR, é mostrado um input para usuário digitar o valor para depósito.
            
            limite_transacoes = transacoes(limite_transacoes)   # Atualiza o valor de limite_transacoes (Pelo deposito)
            if limite_transacoes is False: # Se a variavel for False (Atribuida na def), o programa para
                break
            
            data_transacao_deposito.append(datetime.now())
            
            valor_de_deposito = float(input('Digite o valor para depósito: R$'))
            novo_saldo = depositar(saldo, valor_de_deposito) # A função retorna valor de depósito e a variavel novo_saldo, atualiza o saldo anterior valor.
            
            if novo_saldo != saldo:
                saldo = novo_saldo
                print(f'Saldo atualizado no valor de R$ {saldo}')
                extrato_deposito.append(valor_de_deposito) # Adiciono o valor de depósito em uma lista para ser contabilizado no extrato.
                break
            
        elif opcao_menu == 'E':
            print('='*5 + ' Extrato Bancário ' + '='*5)
            
            if len(extrato_saque) == 0 or len(extrato_saque) == 0: # Se não for feito nenhum depósito e nenhum saque, aparece a mensagem de que não há movimentações.
                print('\nNão há movimentações para o extrato.\n')
                
            for saque, data_saque in extrato_saque, data_transacao_saque:
                print(f'\033[1;31m - {saque} \033[39m{data_saque} ')  # Saída para os saques feitos sairem na coloração vermelha no extrato.
                
            for deposito in extrato_deposito:   # Saída para os depositos feitos sairem na coloração verde no extrato.
                print(f'\033[92m + {deposito}')
                
            print('\033[39m' + '='*28)   # Reset para a cor normal do programa
            
            print(f'Saldo atual: R${saldo}')        # Saldo atual da conta
            break
        
        else:
            print('Opção inválida...\nVoltando ao menu...') # Caso usuario digite algo diferente de: (S/D/E/F), ele dá erro e volta ao menu.
            sleep(2)
            break    
    

"""
OBJETIVOS:

Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquela data (Mostre a data). FEITO

Mostre no extrato, a data e hora de todas as transações.

"""


