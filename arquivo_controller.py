import os
import pandas as pd

def created_arquivo_controller():
    folder = os.getcwd()
    path_folder = os.path.join(folder, 'data/transient')  # Substitua pelo caminho da pasta desejada
    file_path = os.path.join(folder, 'controller.csv')

    # Capturar nomes dos arquivos e remover a extensão
    arquivos = os.listdir(path_folder)

    # Eliminar as palavras indesejadas
    palavras_indesejadas = ['_dataset.csv', 'olist_', 'order_', '_dataset', 'product_', '_name', '_translation', '.csv']
    nomes_limpos = [arquivo for arquivo in arquivos]
    for palavra in palavras_indesejadas:
        nomes_limpos = [nome.replace(palavra, '') for nome in nomes_limpos]

    # Caminho do arquivo CSV a ser salvo
    caminho_arquivo = str(path_folder[0]) + '/' + 'controller.csv'

    # Definir os dados a serem escritos no arquivo CSV
    dados = [
        ["path_transient", "path_raw", "path_trusted", "table_transient", "table_raw", "table_trusted", "table_name", "table_name_temp"]
    ] + [
        [str(path_folder[0]) + "data/transient", str(path_folder[0]) + "data/raw", str(path_folder[0]) + "data/trusted", nome.replace('.csv', ""), nome.replace('.csv', ""), nome.replace('.csv', ""), nome_limp, 'temp_' + nome_limp]
        for nome, nome_limp in zip(arquivos, nomes_limpos)
    ]

    # Salvar o arquivo CSV
    pd.DataFrame(dados).to_csv(file_path, index=False, header=False)
    print('Arquivo controller criado com sucesso!')
created_arquivo_controller()
