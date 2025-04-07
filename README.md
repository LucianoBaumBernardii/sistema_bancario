# Sistema Bancário - Banco BAHIA

Este é um projeto simples em Python que simula um sistema de atendimento bancário via terminal. Ele permite ao usuário realizar operações básicas como **depósito**, **saque**, **visualização de extrato** e **encerramento do atendimento**.

---

## ⚙️ Funcionalidades

- **Depósito**: Permite adicionar valores ao saldo, desde que sejam positivos.
- **Saque**: Possui regras como:
  - Limite de 3 saques por sessão
  - Valor máximo de R$ 500 por saque
  - Saque permitido apenas se houver saldo suficiente
- **Extrato**: Exibe todas as transações realizadas e o saldo atual.
- **Encerrar atendimento**: Opção para sair do sistema simulando contato com o gerente.

---

## Regras de negócio

- O saldo inicial é de **R$ 0,00**
- O limite de saque por operação é **R$ 500**
- O número máximo de saques por sessão é **3**
- Apenas valores **positivos** podem ser depositados ou sacados

---

## Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/LucianoBaumBernardii/sistema_bancario.git
   cd sistema_bancario
