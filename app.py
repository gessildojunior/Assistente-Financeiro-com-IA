import streamlit as st
import openai
import os
from dotenv import load_dotenv
from finance import juros_compostos, simulacao_investimento
from memory import salvar, obter

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("💰 Assistente Financeiro com IA")

user = st.text_input("Pergunte sobre finanças:")

if st.button("Enviar"):

    if "juros" in user:
        valor = 1000
        taxa = 1
        meses = 12
        resultado = juros_compostos(valor, taxa, meses)
        st.write(f"Simulação: R${resultado}")

    elif "investir" in user:
        total = simulacao_investimento(500, 1, 12)
        st.write(f"Total investido: R${total}")

    else:
        contexto = obter()

        resposta = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um assistente financeiro educativo."},
                *contexto,
                {"role": "user", "content": user}
            ]
        )

        texto = resposta.choices[0].message.content
        st.write(texto)

        salvar({"role": "user", "content": user})
        salvar({"role": "assistant", "content": texto})
