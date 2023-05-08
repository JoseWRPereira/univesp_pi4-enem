# ==============================================================================
# Bibliotecas
# ==============================================================================
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st 

np.set_printoptions(suppress=True)
pd.set_option('display.float_format', '{:.2f}'.format)


# ==============================================================================
# Sidebar Streamlit
# ==============================================================================

st.sidebar.markdown("# Análise de dados enem 2021")
st.sidebar.markdown("""---""")

ano = st.sidebar.radio(
    "Analisar dados do ano:",
    ('2022', '2021'),
    horizontal=True)

st.sidebar.markdown("""---""")

treineiro = st.sidebar.radio(
    "Incluir treineiros?",
    ('Sim', 'Não'),
    horizontal=True)

st.sidebar.markdown("""---""")
st.sidebar.markdown("Projeto Integrador IV - UniVESP")



# ==============================================================================
# Layout Streamlit
# ==============================================================================
tab1, tab2, tab3 = st.tabs(['Candidatos', 'Municípios', 'Geral'])


with tab1:
    with st.container():
        st.markdown("# Tab1")
    
with tab2:
    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("Tab2 Col1")

        with col2:
            st.markdown("Tab2 Col2")

with tab3:
    with st.container():
        st.markdown("Tab3 Geral")

