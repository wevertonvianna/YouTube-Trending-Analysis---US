# 📊 YouTube Trending Analysis

Análise exploratória de dados (EDA) dos vídeos em alta (Trending) do YouTube nos Estados Unidos.

Este projeto transforma dados públicos do Kaggle em um dashboard interativo utilizando **Streamlit**, com foco em identificar padrões de visualizações, engajamento e categorias mais populares.

---
## 🚀 Acesse o Dashboard Online:



## 🎯 Objetivo

Responder às seguintes perguntas:

- Quais categorias possuem maior média de visualizações?
- Quais categorias geram mais engajamento?
- Existe correlação entre views, likes e comentários?
- O que caracteriza um vídeo trending?

---

## 📂 Estrutura do Projeto

    youtube-trending-analysis/
    │
    ├── data/
    │   ├── USvideos.csv
    │   ├── US_category_id.json
    │
    ├── app.py
    ├── requirements.txt
    └── README.md

---

## 🛠 Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Streamlit
- Matplotlib
- Seaborn

---

## 📊 Métricas Criadas

### 🔹 Engagement Rate

    engagement = (likes + comment_count) / views

Essa métrica mede o nível de interação proporcional ao número de visualizações.

---

## 📈 Principais Análises

- Média de visualizações por categoria
- Engajamento médio por categoria
- Correlação entre views, likes e comentários
- Visualização interativa via dashboard

---

## ▶ Como Executar

1️⃣ Clone o repositório:

    git clone https://github.com/SEU_USUARIO/youtube-trending-analysis.git

2️⃣ Instale as dependências:

    pip install -r requirements.txt

3️⃣ Execute o app:

    streamlit run app.py

---

## 📌 Dataset

Fonte:  
Kaggle — Trending YouTube Video Statistics  
https://www.kaggle.com/datasets/datasnaek/youtube-new

---

## 🚀 Possíveis Melhorias Futuras

- Modelo preditivo de visualizações
- Análise de sentimento dos títulos (NLP)
- Dashboard com filtros interativos
- Deploy em produção (Streamlit Cloud)

---

## 👨‍💻 Autor

**Weverton Vianna Ferreira**  
LinkedIn: https://www.linkedin.com/in/weverton-vianna-ferreira  
GitHub: https://github.com/wevertonvianna
