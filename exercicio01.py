# Sistema de perguntas e respostas com Python

perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '7',
            'd': '10',
            'e': '15',
        },
        'resposta_certa': 'b'
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 5x45? ',
        'respostas': {
            'a': '550',
            'b': '425',
            'c': '225',
            'd': '650',
            'e': '175',
        },
        'resposta_certa': 'c'
    },
    'pergunta 3': {
        'pergunta': 'Quanto é 80/6? ',
        'respostas': {
            'a': '12',
            'b': '15.2',
            'c': '17',
            'd': '10,3',
            'e': '13,33',
        },
        'resposta_certa': 'e'
    }
}
print()

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    print()
