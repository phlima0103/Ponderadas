import streamlit as st
import pandas as pd
import altair as alt

# Carregar os dados do arquivo CSV
df = pd.read_csv("dados_ficticios.csv")

# Configuração do título do app
st.title("Análise de Dados com Streamlit")

# Exibir tabela
st.subheader("Dados Carregados")
st.dataframe(df)

# Gráfico de barras: Quantidade por Categoria
st.subheader("Gráfico de Barras: Quantidade por Categoria")
bar_chart = alt.Chart(df).mark_bar().encode(
    x=alt.X("Categoria", title="Categoria"),
    y=alt.Y("Quantidade", title="Quantidade"),
    color="Categoria"
)
st.altair_chart(bar_chart, use_container_width=True)

# Gráfico de linha: Evolução do Valor ao longo do tempo
st.subheader("Gráfico de Linha: Evolução do Valor ao Longo do Tempo")
df["Data"] = pd.to_datetime(df["Data"])
line_chart = alt.Chart(df).mark_line().encode(
    x=alt.X("Data", title="Data"),
    y=alt.Y("Valor", title="Valor"),
    tooltip=["Data", "Valor"]
)
st.altair_chart(line_chart, use_container_width=True)

# Filtros
st.subheader("Filtros de Dados")
categoria_selecionada = st.selectbox("Selecione uma Categoria:", options=df["Categoria"].unique())
df_filtrado = df[df["Categoria"] == categoria_selecionada]
st.write("Dados Filtrados:")
st.dataframe(df_filtrado)

st.subheader("Gráfico Filtrado: Quantidade por Data")
bar_filtered_chart = alt.Chart(df_filtrado).mark_bar().encode(
    x=alt.X("Data:T", title="Data"),
    y=alt.Y("Quantidade", title="Quantidade"),
    color="Categoria"
)
st.altair_chart(bar_filtered_chart, use_container_width=True)
