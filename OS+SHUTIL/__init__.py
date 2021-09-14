import os
import shutil

caminho_original = r'E:\testandoPy'
caminho_novo = r'E:\testandoPy2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta: {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        os.remove(new_file_path)
        print(f'Os arquivosem {new_file_path} foram apagados.')

