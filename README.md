# sistema-bancario
Sistema Bancário Avançado em Python

# Sistema Bancário Avançado em Python

Projeto desenvolvido com foco na aplicação de conceitos avançados de programação em Python, incluindo Programação Orientada a Objetos (POO), arquitetura modular, decoradores para registro de logs, geradores para eficiência de memória e iteradores customizados.

---

## Recursos e Destaques Técnicos

### 1. Decorador de Log (`@log_transacao`)
Utilização de **Decoradores** para rastreabilidade auditável das operações bancárias (saque, depósito, criação de conta). A função intercepta a execução e registra automaticamente data, hora e o tipo de transação executada.

### 2. Gerador de Relatórios (`yield`)
Implementação de **Gerador de Histórico** para otimização de consumo de memória. Permite filtrar o extrato da conta por tipo de transação (ex: saques ou depósitos) processando os dados sob demanda.

### 3. Iterador Personalizado (`ContaIterador`)
Criação de uma classe **Iteradora** para percorrer a lista de contas ativas no sistema, aplicando os métodos especiais `__iter__` e `__next__` para formatar e exibir os dados dos titulares de forma elegante.

---


# Execute o arquivo principal
python main.py
