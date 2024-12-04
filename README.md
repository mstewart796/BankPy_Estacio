# BankPy

BankPy is a simple Python application that emulates a banking system. Users can create accounts, manage their money through deposits, withdrawals, and transfers, and view a list of all registered accounts. The application features a user-friendly command-line interface for seamless interaction.

## Features

- **Create Account**: Register a new account with customer details including name, email, CPF (Brazilian ID), and date of birth.
- **Deposit Money**: Add funds to your account securely.
- **Withdraw Money**: Withdraw money with a validation mechanism to prevent overdrawing.
- **Transfer Money**: Transfer funds between two accounts, ensuring sufficient balance and account validity.
- **List Accounts**: View all registered accounts with their details.
- **Validation**: Includes input validation for all user-provided details like email, CPF, and date of birth.
- **Error Handling**: Implements `try/except` blocks to handle invalid inputs gracefully.

## How to Run the Application

### Prerequisites

- Python 3.7 or higher
- Basic knowledge of Python and command-line tools

### Running the Application

Run the `banco.py` file:
```bash
python banco.py
```

The application will display a menu with options to manage your bank account:

1. Create Account
2. Withdraw Money
3. Deposit Money
4. Transfer Money
5. List Accounts
6. Exit

Simply follow the prompts to interact with the application.

## Code Structure

- **`banco.py`**: Main script that provides the user interface and coordinates user actions.
- **`models/cliente.py`**: Contains the `Cliente` class to manage customer details.
- **`models/conta.py`**: Contains the `Conta` class to manage account operations like deposit, withdrawal, and transfer.

## Highlights

- **Data Validation**:
  - Ensures CPF follows the format `XXX.XXX.XXX-XX`.
  - Validates email format with regex.
  - Checks date of birth format (`DD/MM/YYYY`).
- **Clean Code**:
  - Modular design with separate functions for core features.
  - Comprehensive comments for easier understanding.
- **User Feedback**:
  - Informative messages and progress indicators (e.g., `Volte sempre`, `Conta criada com sucesso`).

## Example

### Creating an Account:
```plaintext
Informe os dados do cliente:
Nome: Martin Stewart
Email: martin@example.com
CPF (digite no formato xxx.xxx.xxx-xx): 123.456.789-00
Data de nascimento (dd/mm/aaaa): 01/11/1990
Conta criada com sucesso
```

### Listing Accounts:
```plaintext
Listagem de contas
Número da Conta: 1
Cliente: Martin Stewart
Saldo: R$ 0.00
--------
```

## Future Improvements

- Add persistent storage to save account details across sessions.
- Implement password protection for accounts.
- Create a graphical user interface (GUI) for better user experience.
- Add internationalization (e.g., multilingual support).

## Acknowledgments

This project was initially developed as part of a Python course with Geek University and enhanced further during my **Rapid Application Development with Python** university course at **Universidade Estácio de Sá**.
