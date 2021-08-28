from eletronico import Eletronico
from log import Logmixin


class Smarthphone(Eletronico, Logmixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não está ligado.'
            print(info)
            self.log_info(info)
            return

        if self._conectado:
            error = f'{self._nome} Já está conectado.'
            print(error)
            self.log_info(error)
            return

        info = f'{self._nome} Está conectado!'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} NÃO ESTÁ CONECTADO.'
            print(error)
            self.log_info(error)
            return

        info = f'{self._nome} foi desligado com sucesso.'
        print(info)
        self.log_info(info)
        self._conectado = False
