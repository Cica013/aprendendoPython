# https://rszalski.github.io/magicmethods

class A:
    def __new__(cls, *args, **kwargs):

        if hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)

        return super().__new__(cls)

    def __init__(self):
        print('Eu sou o INIT')


a = A()

