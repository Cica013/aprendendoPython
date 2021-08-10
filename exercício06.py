"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)

    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1', <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer

"""
cont = 1
while True:
    tarefas = []
    tarefa = input('Deseja fazer esta tarefa sim(S) ou não(N)? ').strip().upper()
    if tarefa == 'S':
        print('Feita!')
        tarefas.append(f'Tarefa {cont}')
        print(tarefas)
        print()
        while True:
            escolha = input('Deseja adicionar tarefa sim(S) ou não(N)? ').strip().upper()
            if escolha == 'S':
                tarefa_1 = input('Deseja fazer esta tarefa sim(S) ou não(N)? ').strip().upper()
                if tarefa_1 == 'S':
                    cont += 1
                    print('Feita!')
                    tarefas.append(f'Tarefa {cont}')
                    print(tarefas)
                    print()
                elif tarefa_1 == 'N':
                    print(tarefas)
                    print('Fim!')
                    break
                else:
                    print('Você digitou algo errado ai... vamos voltar.')
                    print()
                    continue
            elif escolha == 'N':
                print(tarefas)
                print('Acabou aqui!')
                print()
                break
            else:
                print('Você digitou algo errado ai... vamos voltar.')
                print()
                continue
            desfaz = input('Deseja desfazer? (S) ou (N): ').strip().upper()
            if desfaz == 'S':
                tarefas.pop()
                print(tarefas)
            elif desfaz == 'N':
                pass
            refazer = input('Deseja refazer? (S) ou (N): ').strip().upper()


    elif tarefa == 'N':
        print(tarefas)
        print('Fim!')
        print()
        break
    else:
        print('Você digitou algo errado ai... Vamos voltar')
