class A:
    vc = 123

    def __init__(self):
        pass


a1 = A()
a2 = A()
a3 = A()

a1.vc = 321

print(a1.vc)
print(a2.vc)
print(a3.vc)
print(A.vc)
