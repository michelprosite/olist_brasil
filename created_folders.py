import pandas as pd
import os

def created_folders():
    # Variavel responsável pos capiturar o path raiz do projeto
    path_folder = os.getcwd() 
    # Abrindo e carregando o arquivo CSV com os nomes das pastas que serão criadas para o projeto
    file_path = os.path.join(path_folder, 'nome_diretorios.csv')
    f = pd.read_csv(file_path)
    lista_folders = f['Folders'].to_list()

    #Criando o diretório "data"
    if not os.path.exists('data'):
            os.makedirs('data')

    # Laço for percorre a lista das partas cridas e inicia as pastas do projeto
    for i in lista_folders:
        diretorio = path_folder

        # Verifica se as pastas já foram criadas, se não, as cria.
        if not os.path.exists(diretorio + '/data/' + i):
            os.makedirs(diretorio + '/data/' + i)
            print(f"Diretório {i} criado com sucesso!")
        else:
            print(f"O diretório {i} já existe.")
created_folders()