class Notebook:
    # atributo da classe
    fonte = 'fonte de 30W'

    # método
    def __init__(self, nome_notebook, marca, processador, ram, tipo_armazenamento, qtd_armazenamento, gpu, monitor,
                 cor, ligar_desligar=False, ):
        self.nome_notebook = nome_notebook
        self.marca = marca
        self.processador = processador
        self.ram = ram
        self.tipo_armazenamento = tipo_armazenamento
        self.qtd_armazenamento = qtd_armazenamento
        self.gpu = gpu
        self.monitor = monitor
        self.cor = cor
        self.ligar_desligar = ligar_desligar

    # método
    def ligar(self):
        if self.ligar_desligar:
            print('Já estou ligado!')
            return
        print('Estou ligando...')
        self.ligar_desligar = True

    # método
    def desligar(self):
        if not self.ligar_desligar:
            print('Já estou desligado!')
            return
        print('Desligando...')
        self.ligar_desligar = False

    # método
    def exibir_especificacoes(self):
        print(
            '\033[1;4;3;32mEspecificações técnicas:\033[m \n'
            f'Modelo:\t\t{self.nome_notebook},\nMarca:\t\t{self.marca},\nProcessador:\t\t{self.processador},\n'
            f'Memória ram:\t\t{self.ram},\nTipo armazenamento:\t\t{self.tipo_armazenamento},'
            f'\nQtd armazenamento:\t\t{self.qtd_armazenamento},\nPlaca de vídeo:\t\t{self.gpu},'
            f'\nMonitor:\t\t{self.monitor},\nCor:\t\t{self.cor}')
