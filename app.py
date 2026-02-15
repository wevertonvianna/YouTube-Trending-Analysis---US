import streamlit as st
import pandas as pd
import json

st.title("📊 YouTube Trending Analysis-US")

# Carregar dados
@st.cache_data
def load_data():
    videos = pd.read_csv("data/USvideos.csv")

    with open("data/US_category_id.json") as f:
        data = json.load(f)

    categorias = pd.json_normalize(data["items"])[["id","snippet.title"]]
    categorias.columns = ["category_id","category_name"]
    categorias["category_id"] = categorias["category_id"].astype(int)

    df = videos.merge(categorias, on="category_id")

    df["engagement"] = (df["likes"] + df["comment_count"]) / df["views"]

    return df

df = load_data()

# Mostrar dados
if st.checkbox("Mostrar dados brutos"):
    st.write(df.head())

# 📊 Média de views por categoria
st.subheader("Média de Views por Categoria")

media_views = df.groupby("category_name")["views"].mean().sort_values(ascending=False)

st.bar_chart(media_views)

# 📊 Engajamento
st.subheader("Engajamento Médio por Categoria")

engajamento = df.groupby("category_name")["engagement"].mean().sort_values(ascending=False)

st.bar_chart(engajamento)

# 📈 Correlação
st.subheader("Correlação")

st.write(df[["views","likes","comment_count"]].corr())
