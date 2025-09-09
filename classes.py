from abc import ABC, abstractmethod

class Account(ABC): #* Classe Abstrata
    def __init__(self, agency, num_account, balance):
        self.agency = agency
        self.num_account = num_account
        self.balance = balance
        self.limit = 1000

    #* Método de depositar dinheiro na conta (Sem limite definido)
    def deposit(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            print('Invalid value.')
        else:
            self.balance += value
            print(f'You deposited ${value} in your account.')
        print(f'Your balance is ${self.balance}.')
    
    #* Método abstrado: (Vai ser setado nas subclasses através do polimorfismo)
    @abstractmethod
    def withdraw(self, value): 
        raise NotImplementedError('Withdraw Not Implemented. Please Implement this method')


class CurrentAccount(Account): #* Conta Corrente (Herdado de Conta)
    def __init__(self, agency, num_account, balance):
        super().__init__(agency, num_account, balance)
        self.limit = 1500
    
    #* Método de sacar em contas correntes (limite maximo = 1500)
    def withdraw(self, value):
        if value > self.balance:
            print('Insuficient Balance.')
        elif not isinstance(value, (int, float)):
            print('Invalid value.')
        else:
            self.balance -= value
            self.limit -= value
            print(f'You withdraw ${value} in your account.')
        print(f'Balance: ${self.balance}.')
        print(f'Your limit: ${self.limit}')



class SavingsAccount(Account): #* Conta Poupança (Herdado de Conta)
    def __init__(self, agency, num_account, balance):
        super().__init__(agency, num_account, balance)

    #* Método de sacar em contas poupanças (limite maximo = 1000 | Padrão)
    def withdraw(self, value):
        if value > self.balance:
            print('Insuficient Balance.')
        elif not isinstance(value, (int, float)):
            print('Invalid value.')
        else:
            self.balance -= value
            self.limit -= value
            print(f'You withdraw ${value} in your account.')
        print(f'Balance: ${self.balance}.')
        print(f'Your limit: ${self.limit}')
        

#? PARTE DE PESSOA / CLIENTE
class Person(ABC):
    def __init__(self, name, age):
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



#? PARTE DE BANCO
class Bank():
    def __init__(self, client, account):
        self.client = client
        self.account = account
    
    def _auth(self):
        if self.client:
            ...
