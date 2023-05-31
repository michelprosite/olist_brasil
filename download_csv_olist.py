import os
import kaggle

def download_csv_olist():
    folder = os.getcwd()
    path_folder = os.path.join(folder, 'data/transient')

    files = os.listdir(path_folder)

    if len(files) == 0:
        PATH_FOLDER = path_folder
        os.environ['PATH_FOLDER'] = PATH_FOLDER

        kaggle.api.dataset_download_files('olistbr/brazilian-ecommerce', path=PATH_FOLDER, unzip=True)
        print('Arquivos carregados e descompactados.')
    else:
        print()
        print(f'Arquivos já existem e ou foram atualizados!')
        print('Caso queira atualiza-los se faz necessário executar a recarga da Raw para zerar os arquivos.')
download_csv_olist()
