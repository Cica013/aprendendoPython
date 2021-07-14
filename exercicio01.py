# Sistema de perguntas e respostas com Python

acertos = 0
perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '7', 'd': '10', 'e': '15',},
        'resposta_certa': 'b'
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 5x45? ',
        'respostas': {'a': '550', 'b': '425', 'c': '225', 'd': '650', 'e': '175',},
        'resposta_certa': 'c'
    },
    'pergunta 3': {
        'pergunta': 'Quanto é 80/6? ',
        'respostas': {'a': '12', 'b': '15.2', 'c': '17', 'd': '10,3', 'e': '13,33',},
        'resposta_certa': 'e'
    }
}
print()

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print()
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    print()

    resposta_usuario = input('Digite a sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        acertos += 1
        print('A resposta esta...   CERTAA!!! :D')
    else:
        print('A resposta está...     ERRADA!!! :(')

qtd_perguntas = len(perguntas)
porcentagem_acerto = acertos / qtd_perguntas * 100
print(f'Você teve uma taxa de {porcentagem_acerto:.1f}% de acerto.')
