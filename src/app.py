import streamlit as st
import contract
from datetime import datetime, time

def main():
    st.title("Sist. de CRM Zap - Simples")
    email = st.text_input("Email Vendedor: ")
    data = st.date_input("Data da Venda: ", datetime.now(), format="DD/MM/YYYY")
    hora = st.time_input("Hora da Venda: ", value=time(9, 0))
    valor = st.number_input("Valor da Venda: ", min_value=0.00, format="%.2f")
    quantidade = st.number_input("Quantidade de Produtos Vendidos: ", min_value=1, step=1)
    produto = st.selectbox("Produto Vendido", options=["Zap com Gemini", "Zap com GPT", "Zap com Llama3"])

    if st.button("Salvar"):
        data_hora = datetime.combine(data, hora)
        st.write("Dados da Venda:**")
        st.write(f"Email do vendedor: {email}")
        st.write(f"Data e Hora da Compra: {data_hora}")
        st.write(f"Valor da Venda: R$ {valor:.2f}")
        st.write(f"Quantidade de Produtos: {quantidade}")
        st.write(f"Produto: {produto}")


if __name__ == "__main__":
    main()  