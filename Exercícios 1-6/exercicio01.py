# Sistema de perguntas e respostas com Python

acertos = 0
perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '7', 'd': '10', 'e': '15', },
        'resposta_certa': 'b'
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 5x45? ',
        'respostas': {'a': '550', 'b': '425', 'c': '225', 'd': '650', 'e': '175', },
        'resposta_certa': 'c'
    },
    'pergunta 3': {
        'pergunta': 'Quanto é 80/6? ',
        'respostas': {'a': '12', 'b': '15.2', 'c': '17', 'd': '10,3', 'e': '13,33', },
        'resposta_certa': 'e'
    },
    'pergunta 4': {
        'pergunta': 'Quanto é (5X6)/2? ',
        'respostas': {'a': '15', 'b': '17', 'c': '12', 'd': '10,5', 'e': '13,33', },
        'resposta_certa': 'a'
    },
    'pergunta 5': {
        'pergunta': 'Quanto é 80-32? ',
        'respostas': {'a': '38', 'b': '27', 'c': '52', 'd': '48', 'e': '61', },
        'resposta_certa': 'd'
    },
    'pergunta 6': {
        'pergunta': 'Quanto é 1.124/6? ',
        'respostas': {'a': '120', 'b': '214,2', 'c': '178,3', 'd': '101,3', 'e': '187,33', },
        'resposta_certa': 'e'
    },

    'pergunta 7': {
        'pergunta': 'Quanto é 55+66? ',
        'respostas': {'a': '121', 'b': '150.2', 'c': '130', 'd': '87,3', 'e': '139,33', },
        'resposta_certa': 'a'
    },
}
print()

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print()
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    print()

    resposta_usuario = input('Digite a sua resposta: ')
    print()
    if resposta_usuario == pv['resposta_certa']:
        acertos += 1
        print('A resposta esta...   CERTAA!!! :D')
    else:
        print('A resposta está...     ERRADA!!! :(')
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = (acertos / qtd_perguntas) * 100
print(f'Você acertou {acertos} perguntas, ficou com uma taxa de {porcentagem_acerto:.1f}% de acerto.')
if porcentagem_acerto == 100:
    print('Não acredito, você acertou todas as questões, você é simsplismente incrível.')
elif porcentagem_acerto > 90:
    print('Uaaauuu, você manda muito bem na matemática!')
elif porcentagem_acerto > 60:
    print('Você foi bem, conseguiu acertas muitas questões...')
elif porcentagem_acerto > 50:
    print('Você ficou na média, nem muito bom nem muito ruim... kk')
else:
    print('Nossa, você ficou abaixo da média... poxa vida, que pena... :/')
