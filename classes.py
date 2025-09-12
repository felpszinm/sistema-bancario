from abc import ABC, abstractmethod

class Account(ABC): #* Classe Abstrata
    def __init__(self, agency, num_account, balance) -> None:
        self.agency = agency
        self.num_account = num_account
        self.balance = balance
        self._limit = 1000

    #* Método abstrado: (Vai ser setado nas subclasses através do polimorfismo)
    @abstractmethod
    def withdraw(self, value:float): 
        raise NotImplementedError('Withdraw Not Implemented. Please Implement this method')

    #* Método de depositar dinheiro na conta (Sem limite definido)
    def deposit(self, value:float): 
        if not isinstance(value, (int, float)) or value <= 0:
            print('Invalid value.')
        else:
            self.balance += value
            print(f'You deposited ${value} in your account.')
        print(f'Your balance is ${self.balance}.')
    

#? Tipos de contas: 
class CurrentAccount(Account): #* Conta Corrente (Herdado de Conta)
    def __init__(self, agency, num_account, balance):
        super().__init__(agency, num_account, balance)
        self.__limit = 1500
    
    #* Método de sacar em contas correntes (limite maximo = 1500)
    def withdraw(self, value:float):
        if value >= self._limit:
            print('Insuficient Balance.')
        elif not isinstance(value, float):
            print('Invalid value.')
        else:
            self.balance += -value
            self.__limit -= value
            print(f'You withdraw ${value} in your account.')
        print(f'Balance: ${self.balance}.')
        print(f'Your limit: ${self.__limit}')

class SavingsAccount(Account): #* Conta Poupança (Herdado de Conta)
    def __init__(self, agency, num_account, balance):
        super().__init__(agency, num_account, balance)

    #* Método de sacar em contas poupanças (limite maximo = 1000 | Padrão)
    def withdraw(self, value:float):
        if value >= self._limit:
            print('Insuficient Balance.')
        elif not isinstance(value, float):
            print('Invalid value.')
        else:
            self.balance += -value
            self._limit -= value
            print(f'You withdraw ${value} in your account.')
        print(f'Balance: ${self.balance}.')
        print(f'Your limit: ${self._limit}')


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

class Client(Person): #* Cliente (Herdado de Pessoa)
    def __init__(self, name, age, account):
        super().__init__(name, age)
        self.account = account

    #* Getters para nome e idade do cliente.
    @property
    def client_name(self):
        return self.name

    @property
    def client_age(self):
        return self.age


class Bank():
    def __init__(self, client, account, password: str) -> None:
        self.client = client
        self.account = account
        self._password = password
        self.account_attemps = 3
        self.withdraws_attemps = 3
    
    #* Autenticação da conta do banco de usuario:
    def account_auth(self, num_account:int , password: str):
        if self.account_attemps == 0:
            return 'blocked'
        
        if self.account.num_account != num_account or self._password != password:
                self.account_attemps -= 1
                print(f'Incorrect password or account number. Please check your password.\nYou have more {self.account_attemps} attempts left.')
                return False
        return True


    #* Como cliente e conta está agregado ao Banco, precisamos somente da validação da agência
    def withdraw_auth(self, agency_number:int, password:str):
        print(self.account.agency, type(self.account.agency))
        print(agency_number, type(agency_number))

        print(self._password, type(self._password))
        print(password, type(password))
        
        if self.withdraws_attemps == 0:
            print('Your account is blocked to do withdraws. Try later again.')
            return 'blocked'

        elif self.account.agency != agency_number or self._password != password:
                self.withdraws_attemps -= 1
                print(f'Incorrect agency number or password.\nYou have more {self.withdraws_attemps} attempts')
            
        elif self.account.agency == agency_number and self._password == password:
                return True
                