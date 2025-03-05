# Projeto MoveEat

Este repositório contém o código fonte para o projeto MoveEat, uma aplicação que utiliza Flask e SQL Server para gerenciar dados relacionados à nutrição e exercícios físicos.

## Pré-requisitos

Antes de começar, você precisará instalar o seguinte:

### Driver ODBC 18 para SQL Server

É necessário instalar o Driver ODBC 18 para SQL Server para permitir a autenticação e conexão com o servidor de banco de dados SQL Server. Você pode baixar o driver através do seguinte link:

[Download ODBC Driver 18 for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)

### Biblioteca pyodbc

A biblioteca `pyodbc` é utilizada para conectar-se ao SQL Server a partir do Python. Instale-a usando pip:
pip install pyodbc

Copy code


## Verificando os Drivers Instalados

Para verificar se o driver necessário está instalado, você pode utilizar o seguinte bloco de código Python:

```python
import pyodbc
print(pyodbc.drivers())
Conectando ao Banco de Dados
Para testar a funcionalidade de conexão com o banco de dados, utilize a função connect_to_database definida abaixo:

python
Copy code

def connect_to_database():
    try:
        cnxn = pyodbc.connect(
            "Driver={ODBC Driver 18 for SQL Server};"
            "Server=BRASLBRJ0108KD5;"
            "Database=db_MoveEat;"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )
    except pyodbc.Error as e:
        print("Erro ao conectar ao SQL Server:", e)
        return None
    else:
        print("Conexão estabelecida com sucesso.")
        return cnxn

# Chamada da função
connection = connect_to_database()
Suporte
Para obter ajuda ou relatar problemas, abra uma issue neste repositório GitHub.

Contribuições
Contribuições são bem-vindas! Para contribuir com o projeto, por favor faça um fork do repositório e submeta um pull request com suas alterações.

Licença
Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Copy code


Este bloco de Markdown agora inclui todas as seções e códigos necessários, prontos para serem usados diretamente em um arquivo `README.md`.



