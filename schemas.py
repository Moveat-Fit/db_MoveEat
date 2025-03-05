{
 "cells": [
  {
   "cell_type": "raw",
   "id": "45507bd3-1710-43d4-8bab-d7687dc879f8",
   "metadata": {},
   "source": [
    "import pyodbc\n",
    "\n",
    "def create_database():\n",
    "    try:\n",
    "        # Conectar ao servidor sem especificar um banco de dados\n",
    "        cnxn = pyodbc.connect(\n",
    "            \"Driver={ODBC Driver 18 for SQL Server};\"\n",
    "            \"Server=BRASLBRJ0108KD5;\"\n",
    "            \"Trusted_Connection=yes;\"\n",
    "            \"TrustServerCertificate=yes;\"\n",
    "        )\n",
    "        cnxn.autocommit = True\n",
    "\n",
    "        # Criar um novo cursor\n",
    "        cursor = cnxn.cursor()\n",
    "\n",
    "        # Executar o comando para criar o banco de dados\n",
    "        cursor.execute('CREATE DATABASE db_MoveEat')\n",
    "        print(\"Banco de dados 'db_MoveEat' criado com sucesso.\")\n",
    "\n",
    "        # Fechar o cursor e a conexão\n",
    "        cursor.close()\n",
    "        cnxn.close()\n",
    "\n",
    "    except Exception as e:\n",
    "        print(\"Erro ao criar o banco de dados:\", str(e))\n",
    "\n",
    "# Chamar a função para criar o banco de dados\n",
    "create_database()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e35b6095-7231-4b28-abcc-f7863345d45d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Conexão estabelecida com sucesso.\n"
     ]
    }
   ],
   "source": [
    "def connect_to_database():\n",
    "    try:\n",
    "        cnxn = pyodbc.connect(\n",
    "            \"Driver={ODBC Driver 18 for SQL Server};\"\n",
    "            \"Server=BRASLBRJ0108KD5;\"\n",
    "            \"Database=db_MoveEat;\"\n",
    "            \"Trusted_Connection=yes;\"\n",
    "            \"TrustServerCertificate=yes;\"\n",
    "        )\n",
    "    except pyodbc.Error as e:\n",
    "        print(\"Erro ao conectar ao SQL Server:\", e)\n",
    "        return None\n",
    "    else:\n",
    "        print(\"Conexão estabelecida com sucesso.\")\n",
    "        return cnxn\n",
    "\n",
    "# Chamada da função\n",
    "connection = connect_to_database()"
   ]
  },
  {
   "cell_type": "raw",
   "id": "35b67d72-f5db-435e-b37b-8b9664b3eb3e",
   "metadata": {},
   "source": [
    "def create_tables(cnxn):\n",
    "    sql_commands = [\n",
    "        \"\"\"\n",
    "        CREATE TABLE tb_Users (\n",
    "            UserID INT PRIMARY KEY IDENTITY,\n",
    "            Name NVARCHAR(100),\n",
    "            Email NVARCHAR(100) UNIQUE,\n",
    "            Password NVARCHAR(100),\n",
    "            UserType NVARCHAR(50),  -- 'patient' or 'professional'\n",
    "            DateTime DATETIME DEFAULT GETDATE()\n",
    "        );\n",
    "        \"\"\",\n",
    "        \"\"\"\n",
    "        CREATE TABLE tb_PatientProfile (\n",
    "            PatientID INT PRIMARY KEY IDENTITY,\n",
    "            UserID INT FOREIGN KEY REFERENCES tb_Users(UserID),\n",
    "            BirthDate DATETIME,\n",
    "            Gender NVARCHAR(50),\n",
    "            Height INT,\n",
    "            CurrentWeight INT\n",
    "        );\n",
    "        \"\"\",\n",
    "        \"\"\"\n",
    "        CREATE TABLE tb_ProfessionalProfile (\n",
    "            ProfessionalID INT PRIMARY KEY IDENTITY,\n",
    "            UserID INT FOREIGN KEY REFERENCES tb_Users(UserID),\n",
    "            Specialty NVARCHAR(100),\n",
    "            ProfessionalRegistration NVARCHAR(100),\n",
    "            Description NVARCHAR(255),\n",
    "            YearsExperience INT\n",
    "        );\n",
    "        \"\"\"\n",
    "    ]\n",
    "    cursor = cnxn.cursor()\n",
    "    for sql in sql_commands:\n",
    "        cursor.execute(sql)\n",
    "    cnxn.commit()\n",
    "    print(\"Tabelas criadas com sucesso.\")\n",
    "\n",
    "# Chamada da função\n",
    "connection = connect_to_database()\n",
    "if connection:\n",
    "    create_tables(connection)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9426892e-d5d4-47af-8a64-15d89a66df56",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
