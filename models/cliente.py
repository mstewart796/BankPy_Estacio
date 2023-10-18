from datetime import date
from utils.helper import date_para_str, str_para_date

class Cliente:
    contador: int = 101 # Um contador para gerar códigos únicos para cada cliente começando com número 101

    def __init__(self: object, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__codigo: int = Cliente.contador
        self.__nome: str = nome
        self.__email: str = email
        self.__data_nascimento: date = str_para_date(data_nascimento)
        self.__data_cadastro: date = date.today()
        Cliente.contador += 1

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

    # Método especial para fornecer uma representação em string do objeto Cliente.
    def __str__(self: object) -> str:
        return f'Código: {self.codigo} \nNome: {self.nome} \nData de Nasciment: {self.data_nascimento} ' \
               f'\nCadastro: {self.data_cadastro}'