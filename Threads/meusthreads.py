from time import sleep
from threading import Thread


# class MeuThread(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo
#
#         super().__init__()
#
#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)
#
#
# t1 = MeuThread('Thread 1', 5)
# t1.start()
#
# t2 = MeuThread('Thread 2', 3)
# t2.start()
#
# t3 = MeuThread('Thread 3', 1)
# t3.start()
#
# for i in range(10):
#     print(i)
#     sleep(1)
###############################################

# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto, end=' ')
#
#
# t1 = Thread(target=vai_demorar, args=('{Olá mundo 1}', 4))
# t1.start()
#
# t2 = Thread(target=vai_demorar, args=('{Olá mundo 2}', 2))
# t2.start()
#
# t3 = Thread(target=vai_demorar, args=('{Olá mundo 3}', 6))
# t3.start()
#
# for i in range(21):
#     print(i, end=' ')
#     sleep(.5)
##################################################################
