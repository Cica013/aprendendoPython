"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)

    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1', <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer

"""
todo_list = []
redo_list = []


def add_list(todo, todo_list):
    todo_list.append(todo)


def show_do(todo_list):
    print()
    print('Lista: ', end='')
    print(todo_list)
    print()


def undo(todo_list, redo_list):
    print()
    if not todo_list:
        print()
        print('Não há o que remover.')
        print()
        return
    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def redo(redo_list, todo_list):
    if not redo_list:
        print()
        print('Nada a o que refazer')
        print()
        return
    last_redo = redo_list.pop()
    todo_list.append(last_redo)


while True:
    todo = input('Digite a tarefa ou ls, undo, redo: ').strip().lower()
    if todo == 'ls':
        show_do(todo_list)
        continue
    elif todo == 'undo':
        undo(todo_list, redo_list)
        continue
    elif todo == 'redo':
        redo(redo_list, todo_list)
        continue
    add_list(todo, todo_list)

