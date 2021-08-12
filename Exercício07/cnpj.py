def formata_cnpj(cnpj):
    cnpj = cnpj.replace('-', '')
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj[:-2]
    cnpj = list(cnpj)
    new_cnpj = []
    for x in cnpj:
        new_cnpj.append(int(x))
    return new_cnpj


def formata_cnpj_original(cnpj):
    cnpj = cnpj.replace('-', '')
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('/', '')
    cnpj = list(cnpj)
    new_cnpj = []
    for x in cnpj:
        new_cnpj.append(int(x))
    return new_cnpj


def contagem_5():
    lista = []
    for x in range(5, 1, -1):
        lista.append(x)
    for y in range(9, 1, -1):
        lista.append(y)
    return lista


def contagem_6():
    lista = []
    for x in range(6, 1, -1):
        lista.append(x)
    for y in range(9, 1, -1):
        lista.append(y)
    return lista


def fazendo_validacao(cnpj):
    cnpj = formata_cnpj(cnpj)
    cont_5 = contagem_5()
    soma = 0
    for x, y in zip(cnpj, cont_5):
        soma += x * y
    formula = 11 - (soma % 11)
    if formula > 9:
        cnpj.append(0)
    else:
        cnpj.append(formula)
    cont_6 = contagem_6()
    soma = 0
    formula = 0
    for x, y in zip(cnpj, cont_6):
        soma += x * y
    formula = soma
    if formula > 9:
        cnpj.append(0)
    else:
        cnpj.append(formula)

    return cnpj


def confirma_validacao(cnpj_1, cnpj_2):
    if cnpj_1 == cnpj_2:
        print('O cnpj é VÁLIDO!')
    else:
        print('O cnpj é INVÁLIDO!')


def valida_cnpj(cnpj):
    cnpj_recebido = formata_cnpj_original(cnpj)
    cnpj_validado = fazendo_validacao(cnpj)
    print(f'cnpj que foi passado: {cnpj_recebido}')
    print(f'cnpj verificado: {cnpj_validado}')
    confirma_validacao(cnpj_recebido, cnpj_validado)





