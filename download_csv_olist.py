import os

folder = os.getcwd()
path_folder = os.path.join(folder, 'transient')

files = os.listdir(path_folder)

if len(files) == 0:
    print('diretorio vazio')
else:
    print('diretorio cheio')
