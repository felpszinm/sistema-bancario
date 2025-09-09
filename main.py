from classes import CurrentAccount, Client, Bank
if __name__ == '__main__':
    account = CurrentAccount(123, 321, 1000)
    client = Client('Felipe', '20', account)
    bank = Bank(client, account)
    account.deposit(100)
    account.withdraw(12)