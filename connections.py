{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d8cd8cd4-ab32-4b0d-8c2f-b38d938c4429",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['SQL Server',\n",
       " 'Amazon Redshift (x64)',\n",
       " 'ODBC Driver 17 for SQL Server',\n",
       " 'ODBC Driver 18 for SQL Server']"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pyodbc\n",
    "pyodbc.drivers()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "b94c473c-c709-4606-856f-d3985fb885d3",
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
   "cell_type": "code",
   "execution_count": null,
   "id": "46824e98-9272-4f99-bb1b-b14df2a82748",
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
