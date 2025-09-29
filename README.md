# 🏦 Sistema Bancário em Python

Este projeto é um **simulador interativo de sistema bancário**, desenvolvido em Python, que permite criar contas, realizar operações de depósito e saque, além de gerenciar clientes e autenticação de forma simples e estruturada.

---

## 🚀 Funcionalidades

- **Criação de Conta Bancária**  
  - Conta Corrente (CurrentAccount)  
  - Conta Poupança (SavingsAccount)  

- **Gerenciamento de Clientes**  
  - Cadastro de cliente com informações como nome, CPF e e-mail.  

- **Operações Bancárias**  
  - Depósito  
  - Saque (regras específicas para cada tipo de conta)  

- **Sistema de Login**  
  - Autenticação de clientes para acesso às contas.  

- **Menu Interativo**  
  - Navegação simples no terminal para realizar as operações.  

---

## 🛠️ Estrutura do Projeto

sistema-bancario-main/
│── sistema-bancario-main/
│ ├── .gitignore
│ ├── README.md
│ ├── classes.py # Contém as classes principais (Account, CurrentAccount, SavingsAccount, Client, Bank)
│ ├── main.py # Script principal com o menu interativo

---

## 📂 Arquivos Principais

- **`main.py`**  
  - Importa as classes principais do `classes.py`.  
  - Gera agência e número de conta aleatórios.  
  - Executa o menu principal com opções de criar conta, login e saída.  

- **`classes.py`**  
  - **Account (classe abstrata):** base para contas bancárias.  
    - Atributos: `agency`, `num_account`, `balance`, `_limit`.  
    - Métodos: `deposit(valor)` e `withdraw(valor)` (abstrato).  
  - **CurrentAccount:** herda de `Account`, implementa regras de conta corrente.  
  - **SavingsAccount:** herda de `Account`, implementa regras de conta poupança.  
  - **Client:** representa os dados do cliente.  
  - **Bank:** gerencia contas, autenticação e clientes.  

---

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd sistema-bancario-main

2. Execute o script principal:
   ```bash
    python main.py

3. Utilize o menu interativo para criar contas e realizar operações bancárias.

---

## 📌 Tecnologias Utilizadas

Python 3

Programação Orientada a Objetos (POO)

Conceitos de Abstração, Herança e Polimorfismo

---

### 👨‍💻 Autor: Felipe Martins
