💼 Sistema Bancário Simples em Python

Este é um sistema bancário simples desenvolvido em Python que permite ao usuário realizar saques, depósitos e visualizar o extrato de transações.
--------------------------------------------------------------------------------------------------------------

✨ Funcionalidades

✅ Depósito: Permite adicionar saldo sem restrição de valor.

💸 Saque: Saques limitados a R$500 por transação e 3 saques diários.

📋 Extrato: Exibe todas as transações realizadas (saques e depósitos) e o saldo atual.

⏳ Sistema de Menu: Interação simples com opções de Saque, Depósito, Extrato e Sair.
--------------------------------------------------------------------------------------------------------------

⚙️ Requisitos:

Para executar este sistema bancário, é necessário ter o Python 3 instalado em seu computador.
--------------------------------------------------------------------------------------------------------------

📚 Como Executar o Programa:

Clone este repositório

git clone https://github.com/seu-usuario/sistema-bancario-python.git

Acesse a pasta do projeto

cd sistema-bancario-python

Execute o programa

python banco.py
--------------------------------------------------------------------------------------------------------------

🗒️ Exemplo de Uso:

Ao iniciar o programa, você verá o seguinte menu:

    	Inicio

    [S] Sacar
    [D] Depositar
    [E] Extrato
    [F] Sair

    =>

Se escolher [D] Depositar, o programa solicitará um valor e atualizará o saldo.

Se escolher [S] Sacar, o programa verificará se o saldo é suficiente e se os limites foram atingidos.

Se escolher [E] Extrato, serão exibidos todos os saques e depósitos.

Se escolher [F] Sair, o programa será encerrado.
--------------------------------------------------------------------------------------------------------------

Exemplo de Execução:

Digite o valor para depósito: R$ 500
Saldo atualizado no valor de R$ 1500

Digite o valor de saque: R$ 200
Saldo atualizado no valor de R$ 1300

===== Extrato Bancário =====
- 200
+ 500
=======================
Saldo atual: R$1300

--------------------------------------------------------------------------------------------------------------

📈 Melhorias Futuras

🔢 Implementar interface gráfica

📂 Integrar com banco de dados para persistência

🛠️ Criar testes automatizados para validação
--------------------------------------------------------------------------------------------------------------

👥 Autor

Desenvolvido por Felipe Martins.
