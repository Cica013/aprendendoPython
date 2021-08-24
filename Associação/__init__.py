from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Fernandinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever('Yamaha')

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
