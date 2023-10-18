from models.cliente import Cliente
from utils.helper import formata_float_str_moeda

class Conta:

    codigo: int = 1001 # Um contador para gerar números de conta exclusivos.

    # Atribui número, cliente, saldo, limite
    def __init__(self: object, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100.0
        self.__saldo_total: float = self._calcula_saldo_total
        Conta.codigo += 1

    # Método especial para fornecer uma representação em string do objeto Conta.
    def __str__(self: object) -> str:
        return f'Número da conta: {self.numero} \nCliente: {self.cliente.nome} ' \
               f'\nSaldo Total: {formata_float_str_moeda(self.saldo_total)}'

    # @property é um chamado decorator que define Getter Methods
    @property # Método getter para o número da conta.
    def numero(self: object) -> int:
        return self.__numero

    @property # Método getter para o cliente associado à conta.
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property # Método getter para o saldo da conta.
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter  # Método setter para definir o saldo da conta.
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property # Método getter para o limite de saldo negativo da conta.
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter # Método setter para definir o limite de saldo negativo da conta.
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    @property # Método getter para o saldo total da conta.
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    @saldo_total.setter # Método setter para definir o saldo total da conta.
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor

    @property # Calcula o saldo total da conta (saldo + limite).
    def _calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    # Método para depositar dinheiro na conta.
    def depositar(self: object, valor: float) -> None:
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self._calcula_saldo_total
            print('Efetuado')
        else:
            print('Erro')

    # Método para sacar dinheiro da conta.
    def sacar(self: object, valor: float) -> None:
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.limite = self.limite + restante
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
            print('Saque efetuado')
        else:
            print('Não realizado')

    # Método para transferir dinheiro de uma conta para outra.
    def transferir(self: object, destino: object, valor: float) -> None:
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.saldo = 0
                self.limite = self.limite + restante
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
            print('Transferência efetuada')
        else:
            print('Não realizado')

