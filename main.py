from classes import CurrentAccount, SavingsAccount, Client, Bank
from time import sleep
import random
import os


if __name__ == '__main__':
    #* Pego os numeros aleatorios e unifico eles com join, depois transformo em inteiros.
    agency = random.sample(range(1, 10), 3)
    str_agency = "".join([str(n) for n in agency])
    num_agency = int(str_agency)

    account = random.sample(range(1, 10), 7)
    str_account = "".join([str(a) for a in account])
    num_account = int(str_account)

    while True:
        print('\t\tMENU\t\t\n\nChoose the options\n[1] -> Create Bank Account\n[2] -> Login\n[3] -> Exit')
        user_menu = int(input('>> '))

        #* Criação da conta e do cliente:
        if user_menu == 1:
            print('Write your name and age.')
            user_name = input('Your name: ').lower().capitalize()
            user_age = int(input('Your age: '))
            user_password = input('Create a password: ')

            if user_age < 18:
                print("You're young to create a bank account.")
            else:
                print('\tBANK ACCOUNT\t\t\n\nChoose the options\n[1] -> Current Account\n[2] -> Savings Account\n')
                user_type_account = int(input('>> '))

                if user_type_account == 1:
                    user_account = CurrentAccount(agency=num_agency, num_account=num_account, balance=0)
                elif user_type_account == 2:
                    user_account = SavingsAccount(agency=num_agency, num_account=num_account, balance=0)
                
                user_client = Client(user_name, user_age, user_account)
                user_bank = Bank(user_client, user_account, user_password)
                os.system('cls')
                print(f'Hello {user_name}, your account has created!\nYour agency is: {num_agency}\nYour Account Number is: {num_account}\n')
                break


    print(f'\033[91mWelcome to the StarzBank {user_name}!\033[0m')
    print('\n\tStarzBank\t\t\n\nChoose the options\n[1] -> Login\n[2] -> Exit\n')
    user_menu = int(input('>> '))

    while True:
        if user_menu == 1:
            login_number = int(input('Enter the number account: '))
            login_password = input('Enter the password: ')
            validation = user_bank.account_auth(login_number, login_password)

            if validation == 'blocked':
                print('Your account has blocked.')
                break

            elif validation is True:
                print('Login accepted!')
                sleep(3)

                print('\tBANK ACCOUNT\t\t\n\nChoose the options\n[1] -> Deposit\n[2] -> Withdraw\n')
                user_bank_menu = int(input('>> '))

                if user_bank_menu == 1:
                    print('\tBANK DEPOSIT')
                    value = float(input('Amount to be deposited: $ '))
                    user_account.deposit(value)

                #! Erro aqui
                elif user_bank_menu == 2:
                    print('\tBANK WITHDRAW')
                    user_agency = int(input('Digit your agency: '))
                    user_password = int(input('Digit your password: '))

                    user_bank.withdraw_auth(user_agency, user_password)
                    value = float(input('Amount to be withdrawn: $ '))
                    user_account.withdraw(value)
    
                elif user_menu == 2:
                    print('Program Finished.')
                    break
    
    
#TODO: Verificar o motivo da autenticação do saque estar falhando
