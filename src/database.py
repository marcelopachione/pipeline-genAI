import psycopg2
from psycopg2 import sql
from contract import Vendas
import streamlit as st
from dotenv import load_dotenv
import os

# load vars from file .env
load_dotenv()

# Postgres Config
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Save data to Postgres
def salvar_no_postgres(dados: Vendas):
    """
    Funcao para salvar os dados no Postgres
    """
    try:
        conn = psycopg2.connect(
            host = DB_HOST,
            database = DB_NAME,
            user = DB_USER,
            password = DB_PASS
        )

        cursor = conn.cursor()

        # insert into vendas table
        insert_query = sql.SQL(
            "INSERT INTO app.vendas (email, data, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s)"
        )

        cursor.execute(insert_query, (
            dados.email,
            dados.data,
            dados.valor,
            dados.quantidade,
            dados.produto.value
        ))

        conn.commit()
        cursor.close()
        conn.close()

        st.success("Dados salvos com sucesso no banco de dados")
    
    except Exception as e:
        st.error(f"Erro ao salvar no banco de dados: {e}")