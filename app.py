import streamlit as st
from datetime import date, timedelta

st.title("🥛 Calendário Alimentar Sem Lactose")
st.write("Calendário alimentar para 2 meses")

cardapio = [
    {
        "Café da manhã": "Tapioca com ovo + banana",
        "Lanche": "Maçã + castanhas",
        "Almoço": "Arroz + feijão + frango + salada",
        "Lanche da tarde": "Vitamina de banana com bebida vegetal",
        "Jantar": "Sopa de legumes com frango"
    },
    {
        "Café da manhã": "Cuscuz + ovo + mamão",
        "Lanche": "Pera + amêndoas",
        "Almoço": "Arroz + feijão + carne + legumes",
        "Lanche da tarde": "Tapioca com pasta de amendoim",
        "Jantar": "Omelete com legumes"
    }
]

data_inicial = date(2026, 10, 1)

for dia in range(56):
    data = data_inicial + timedelta(days=dia)
    refeicoes = cardapio[dia % len(cardapio)]

    st.header(f"Dia {dia + 1} — {data.strftime('%d/%m/%Y')}")

    for refeicao, alimento in refeicoes.items():
        st.write(f"**{refeicao}:** {alimento}")

    st.divider()
