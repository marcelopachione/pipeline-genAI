import streamlit as st
from datetime import datetime, time
from contract import Vendas
from pydantic import ValidationError

def main():
    st.title("Sist. de CRM Zap - Simples")
    email = st.text_input("Email Vendedor: ")
    data = st.date_input("Data da Venda: ", datetime.now(), format="DD/MM/YYYY")
    hora = st.time_input("Hora da Venda: ", value=time(9, 0))
    valor = st.number_input("Valor da Venda: ", min_value=0.00, format="%.2f")
    quantidade = st.number_input("Quantidade de Produtos Vendidos: ", min_value=1, step=1)
    produto = st.selectbox("Produto Vendido", options=["Zap com Gemini", "Zap com GPT", "Zap com Llama3"])

    if st.button("Salvar"):
        
        try:
            data_hora = datetime.combine(data, hora)

            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )

            st.write(venda)
        except ValidationError as e:
            st.error(f"Deu erro {e}")

        


if __name__ == "__main__":
    main()  