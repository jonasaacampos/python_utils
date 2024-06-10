import os


def create_file_structure_data_analysis():

    # Lista de diretórios a serem criados
    directories = [
        "data/raw",
        "data/staged",
        "data/processed/analysis",
        "data/processed/reporting",
        "data/meta/logs",
        "data/meta/schemas",
        "data/archive",
    ]

    # Criar os diretórios
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    print("Estrutura de diretórios criada com sucesso!")

    # cria um arquivo de texto com a descrição da estrutura de diretórios

    dir_information = """
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    =-=-=-=-=-=-=-= Estrutura de Diretórios para Organização de Dados =-=-=-=-=-=-=-=
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    1. Diretório Principal 
        data/
    Este é o diretório raiz onde todos os dados serão armazenados.

    2. Dados Brutos (Raw Data)
        data/raw/
    Contém os dados originais, como foram recebidos. Nenhuma modificação ou limpeza deve ser feita aqui.

    3. Dados Processados (Staged Data)
        data/staged/
    Contém dados que foram transformados e limpos, prontos para a próxima etapa do processamento.

    4. Dados Prontos (Processed Data)
        data/processed/
    Contém os dados finais que foram totalmente processados e estão prontos para análise ou carregamento em um sistema de produção.

    5. Metadados e Logs
        data/meta/
    Contém metadados sobre o processamento de dados, como logs, esquemas e outras informações auxiliares.

    6. Backups e Arquivamento
        data/archive/
    Contém backups dos dados em vários estágios ou versões antigas dos dados.

    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    """

    with open("data/meta/logs/directory_structure.txt", "w", encoding="utf-8") as file:
        file.write(dir_information)
        for directory in directories:
            file.write(directory + "\n")
    file.close()
    print("Arquivo de descrição da estrutura de diretórios criado com sucesso!")
