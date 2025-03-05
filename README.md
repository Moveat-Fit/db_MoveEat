# Projeto de Conexão com SQL Server usando Python
Este projeto demonstra como estabelecer uma conexão com um banco de dados SQL Server usando Python e a biblioteca pyodbc.
## Pré-requisitos
1. Python 3.x instalado
2. pip (gerenciador de pacotes do Python)
3. ODBC Driver 18 para SQL Server
## Instalação
### 1. Instale o ODBC Driver 18 para SQL Server
O driver ODBC 18 para SQL Server é necessário para a autenticação do servidor. Você pode baixá-lo do site oficial da Microsoft:
[Download ODBC Driver 18 for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16)
Siga as instruções de instalação fornecidas no site.
### 2. Instale a biblioteca pyodbc
Abra um terminal ou prompt de comando e execute:

pip install pyodbc

## Verificando os drivers instalados
Para ver os drivers ODBC instalados em seu sistema, você pode usar o seguinte código Python:
```python
import pyodbc
print(pyodbc.drivers())
Testando a conexão com o banco de dados
Use o seguinte código para testar a funcionalidade da conexão com o banco de dados:
import pyodbc
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

Este código tentará estabelecer uma conexão com o servidor SQL Server especificado. Se bem-sucedido, ele imprimirá uma mensagem de sucesso; caso contrário, exibirá uma mensagem de erro.
Notas adicionais
Certifique-se de que o servidor SQL Server está acessível a partir da máquina onde você está executando o script.
As credenciais e configurações de conexão no código de exemplo podem precisar ser ajustadas de acordo com o seu ambiente específico.
Sempre mantenha suas credenciais de banco de dados seguras e não as compartilhe publicamente.
Contribuições
Contribuições para este projeto são bem-vindas. Por favor, abra uma issue ou pull request para sugestões ou melhorias.
Licença
[Adicione aqui informações sobre a licença do seu projeto]

Este README fornece uma visão geral do projeto, instruções de instalaçã
