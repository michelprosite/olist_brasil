import os
import subprocess
import pandas as pd

def carregando_raw():
    folder = os.getcwd()
    file_path = os.path.join(folder, 'controller.csv')
    path = pd.read_csv(file_path)
    print('Path criado com base no arquivo controller!')

    for i in range(len(path['path_transient'])):
        # Criando o caminho dos arquivos e diretórios
        diretorio_transient = path['path_transient'][i]
        nome_arquivo_transient = path['table_transient'][i] + '.csv'
        caminho_arquivo_transient = (folder + diretorio_transient + nome_arquivo_transient)

        diretorio_raw = path['path_raw'][i]
        nome_arquivo_raw = path['table_raw'][i] + '.parquet'
        caminho_arquivo_raw = (folder + diretorio_raw + nome_arquivo_raw)

        # Verificando a existência dos arquivos em Transient e carrega na Raw pela primeira vez
        if os.path.exists(caminho_arquivo_transient) and not os.path.exists(caminho_arquivo_raw):
            # Carregando arquivos csv
            df = pd.read_csv(caminho_arquivo_transient)

            # Dropando os duplicados preservando o último atualizado
            df.drop_duplicates(subset=df.columns[0], keep='last', inplace=True)

            # Verifica se o DataFrame não está vazio
            if not df.empty:
                # Salva na Raw convertendo para o formato Parquet
                df.to_parquet(caminho_arquivo_raw)
                print(f"Arquivo Parquet {nome_arquivo_raw} criado: {caminho_arquivo_raw}")
            else:
                print(f"O DataFrame está vazio: {nome_arquivo_raw}")

        # Caso a Raw já tenha sido carregada pela primeira vez, esse código é executado para atualizar os arquivos verificando se algum arquivo foi deletado.
        elif os.path.exists(caminho_arquivo_transient) and os.path.exists(caminho_arquivo_raw):
            # Confere a existência do arquivo, caso deletado, cria novamente
            if not os.path.exists(caminho_arquivo_raw):
                df = pd.read_csv(caminho_arquivo_transient)
                df.drop_duplicates(subset=df.columns[0], keep='last', inplace=True)
                if not df.empty:
                    df.to_parquet(caminho_arquivo_raw)
                    print(f"Arquivo Parquet {nome_arquivo_raw} criado: {caminho_arquivo_raw}")

            # Carregando os DataFrames para concatenar os novos dados
            df1 = pd.read_csv(caminho_arquivo_transient)
            df2 = pd.read_parquet(caminho_arquivo_raw)

            # Concatenando os dados
            df_concatenado = pd.concat([df2, df1], axis=0)

            # Eliminando as duplicatas pelo ID mantendo sempre a última ocorrência
            df_concatenado = df_concatenado.drop_duplicates(subset=df_concatenado.columns[0], keep='last')
            df_concatenado.to_parquet(caminho_arquivo_raw)
        else:
            print(f'Arquivo Raw {nome_arquivo_raw} já existe! Para atualizá-lo, carregue a transient correspondente.')

        # Após a criação e atualização dos dados, os arquivos Transient são eliminados deixando o diretório
    # livre para receber novos dados
    for i in range(len(path['path_transient'])):
        diretorio_transient = path['path_transient'][i]
        nome_arquivo_transient = path['table_transient'][i] + '.csv'
        caminho_arquivo_transient = os.path.join(diretorio_transient, nome_arquivo_transient)

        if os.path.exists(caminho_arquivo_transient):
            os.remove(caminho_arquivo_transient)

    print("Arquivos Transient eliminados.")

carregando_raw()
