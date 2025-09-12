from abc import ABC, abstractmethod

class Account(ABC): #* Classe Abstrata
    def __init__(self, agency: int, num_account: int, balance: float) -> None:
        self.agency = agency
        self.num_account = num_account
        self.balance = balance
        self._limit = balance

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
            self._limit += self.balance
            print(f'You deposited ${value} in your account.')
        print(f'Your balance is ${self.balance}.')
    

#? Tipos de contas: 
class CurrentAccount(Account): #* Conta Corrente (Herdado de Conta)
    def __init__(self, agency, num_account, balance):
        super().__init__(agency, num_account, balance)
        self.__limit = self._limit + 500 
    
    #TODO:
    #* Método de sacar em contas correntes (limite maximo = 1500)
    def withdraw(self, value:float):
        if value > self.__limit or self.__limit <= 0 or not isinstance(value, float):
            return False
        else:
            self.balance -= value
            self.__limit -= value
            print(f'\nYou withdraw ${value} in your account.')
            print(f'Balance: ${self.balance}.')
            print(f'Your withdraw credit: ${self.__limit}')
            return True

class SavingsAccount(Account): #* Conta Poupança (Herdado de Conta)
    def __init__(self, agency, num_account, balance):
        super().__init__(agency, num_account, balance)

    #* Método de sacar em contas poupanças (limite maximo = 1000 | Padrão)
    def withdraw(self, value:float):
        if value > self._limit or self._limit <= 0 or not isinstance(value, float):
            return False
        else:
            self.balance -= value
            self._limit -= value
            print(f'\nYou withdraw ${value} in your account.')
            print(f'Balance: ${self.balance}.')
            print(f'Your withdraw credit: ${self._limit}')
            return True


class Person:
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age
    
    #* Getters e setters para nome e idade do cliente.
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name:str):
        self.name = self._name
    
    @property
    def age(self):
        return self.age
    
    @age.setter
    def age(self, age: int):
        return self._age
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.name!r}), {self.age!r}'
        return f'{class_name}{attrs}'


class Client(Person): #* Cliente (Herdado de Pessoa)
    def __init__(self, name, age, account):
        super().__init__(name, age)
        self.account = account



class Bank():
    def __init__(self, client, account, password: str) -> None:
        self.client = client
        self.account = account
        self._password = password
        self.account_attemps = 3
        self.withdraws_attemps = 3
    
    #* Autenticação da conta do banco de usuario:
    def account_auth(self, num_account:int , password: str):
        if self.account_attemps == 1:
            return 'blocked'
        
        elif self.account.num_account != num_account or self._password != password:
                self.account_attemps -= 1
                print(f'Incorrect password or account number. Please check your password.\nYou have more {self.account_attemps} attempts left.')
                return False
        return True


    #* Como cliente e conta está agregado ao Banco, precisamos somente da validação da agência
    def withdraw_auth(self, agency_number:int, password:str):
        
        if self.withdraws_attemps == 0:
            print('Your account is blocked to do withdraws. Try later again.')
            return 'blocked'

        elif self.account.agency != agency_number or self._password != password:
                self.withdraws_attemps -= 1
                print(f'Incorrect agency number or password.\nYou have more {self.withdraws_attemps} attempts')
            
        elif self.account.agency == agency_number and self._password == password:
                return True
                