from classes import Account, CurrentAccount, SavingsAccount, Client, Bank
if __name__ == '__main__':
    ''' TODO: Decidir como vai ser colocado as variaveis e criar um while.
    agency = 
    num_account = 
    name = 
    age = 
    '''
    account = CurrentAccount(123, 321, 1000)
    client = Client('Felipe', '20', account)
    bank = Bank(client, account)
    account.deposit(100)
    account.withdraw(12)
    bank._auth() # TODO: Implementar como vai ser feito a verificação da agencia