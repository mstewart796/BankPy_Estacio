from datetime import date
from utils.helper import date_para_str, str_para_date
import csv

class Cliente:
    contador: int = 101 # Um contador para gerar códigos únicos para cada cliente começando com número 101

    def __init__(self: object, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__codigo: int = Cliente.contador
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__email: str = email
        self.__data_nascimento: date = str_para_date(data_nascimento)
        self.__data_cadastro: date = date.today()
        Cliente.contador += 1
        # Salvar os detalhes do cliente em um arquivo CSV quando um novo objeto é criado
        self.save_to_csv()

    # @property é um chamado decorator que define Getter Methods
    @property # Método getter para o código do cliente.
    def codigo(self: object) -> int:
        return self.__codigo

    @property # Método getter para o nome do cliente.
    def nome(self: object) -> str:
        return self.__nome

    @property # Método getter para o email do cliente.
    def email(self: object) -> str:
        return self.__email

    @property # Método getter para o CPF
    def cpf(self: object) -> str:
        return self.__cpf

    @property # Método getter para a data de nascimento formatado como string.
    def data_nascimento(self: object) -> str:
        return date_para_str((self.__data_nascimento))

    @property # Método getter para a data de cadastro formatada como string.
    def data_cadastro(self: object) -> str:
        return date_para_str(self.__data_cadastro)

    def __str__(self: object) -> str:
        return f'Código: {self.codigo} \nNome: {self.nome} \nData de Nasciment: {self.data_nascimento} ' \
               f'\nCadastro: {self.data_cadastro}'
        # Adicione um novo método para salvar os detalhes do cliente em um arquivo CSV

    def save_to_csv(self):
        # Crie ou abra o arquivo CSV para adicionar dados
        with open('clientes.csv', 'a', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([self.__codigo, self.__nome, self.__email, self.__cpf, self.data_nascimento])