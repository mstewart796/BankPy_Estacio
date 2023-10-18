from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []


def main() -> None:
    menu()

def menu() -> None:
    print_title('Banco Martin')

    while True:
        print('Selecione uma opção:')
        print('1 - Criar Conta')
        print('2 - Efetuar saque')
        print('3 - Efetuar depósito')
        print('4 - Efetuar transferência')
        print('5 - Listar contas')
        print('6 - Sair do sistema')


        # Usando try/except para que quando um usuário digite um non-int ele receb um erro
        try:
            opcao: int = int(input())

            if opcao == 1:
                criar_conta()
            elif opcao == 2:
             efetuar_saque()
            elif opcao == 3:
                efetuar_deposito()
            elif opcao == 4:
                efetuar_transferencia()
            elif opcao == 5:
                listar_contas()
            elif opcao == 6:
                print('Volte sempre')
                sleep(2)
                exit(0)
            else:
                print('Opção inválida')
                sleep(2)
                menu()
        except ValueError:
            print('Por favor, digite um número válido (1 - 6).')

# Método para criar uma nova conta e cliente.
def criar_conta() -> None:
    print('Informe os dados do cliente: ')

    nome: str = input('Nome: ')
    email: str = input('Email: ')
    cpf: str = input('CPF: ')
    data_nascimento: str = input('Data de nascimento: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso')
    print('----------')
    sleep(2)
    menu()

# Método para efetuar um saque na conta.
def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com número {numero}')
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()

# As funções 'efetuar_deposito' e 'efetuar_transferencia' têm estrutura semelhante à 'efetuar_saque' e são usadas
# para realizar depósitos e transferências de dinheiro.
def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito: '))

            conta.depositar(valor)
        else:
            print(f'Não foi encontrada a conta com número {numero}')
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da sua conta: '))

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input('Informe o número da conta destino: '))

            conta_d = Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informe o valor da transferência: '))

                conta_o.transferir(conta_d, valor)
            else:
                print(f'Não foi econtrada a conta destino com número {numero_d}')

        else:
            print(f'Não foi econtrada a sua conta com número {numero_o}')
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()

# Método para listar as contas e seus detalhes.
def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas')

        for conta in contas:
            print(conta)
            print('--------')
            sleep(1)
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()

# Método para buscar uma conta pelo número da conta.
def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c =conta
    return c


# Essa função criar cria um t[itulo de 3 linhas, cada linha tem o mesmo número de caracteres
def print_title(title: str) -> None:
    line_length = len(title) + 6  # Adjust for padding spaces
    print('=' * line_length)
    print(f'== {title} ==')
    print('=' * line_length)

# Função para imprimir um título com linhas de separação.
if __name__ == '__main__':
    main()

