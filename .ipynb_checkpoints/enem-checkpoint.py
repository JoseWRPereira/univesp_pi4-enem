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
# Carga de dados
# ==============================================================================

ano = 2022
df = pd.read_csv("./dados/uDados_{}.csv".format(ano), sep=';', encoding='ISO-8859-1')


df_faixa_etaria = pd.DataFrame()
labels = ['< 17','17','18','19','20','21','22','23','24','25','26 a 30','31 a 35','36 a 40','41 a 45','46 a 50','51 a 55','56 a 60','61 a 65','66 a 70','> 70']
df_faixa_etaria['FAIXA_ETARIA'] = labels

if treineiro == 'Sim':
    dfaux = df.loc[df['IN_TREINEIRO']==0]
else:
    dfaux = df

# ==============================================================================
# Layout Streamlit
# ==============================================================================
tab1, tab2, tab3 = st.tabs(['Candidatos', 'Municípios', 'Geral'])


with tab1:
    with st.container():
        st.markdown("# Tab1")
    
        aux = dfaux[['NU_INSCRICAO','TP_FAIXA_ETARIA']].groupby('TP_FAIXA_ETARIA').count().reset_index()
        df_faixa_etaria['CANDIDATOS'] = aux['NU_INSCRICAO']
        df_faixa_etaria.plot( kind='bar', x='FAIXA_ETARIA');

    
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

