# public, protected, private
# _ protected (Não acessar)
# __ private (Não deve ser acessada de maneira alguma.)

class BaseDeDados:
    def __init__(self):
        # Atributo público
        self.__dados = {}

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(f'ID: {id} Nome: {nome}')
            print('-' * 20)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_clientes(1, 'Otávio')
bd.inserir_clientes(2, 'Silvanis')
bd.inserir_clientes(3, 'Islaine')
bd.__dados = 'Outra coisa'
bd.apaga_cliente(1)
bd.lista_clientes()
#print(bd.__dados)
#print(bd._BaseDeDados__dados)

