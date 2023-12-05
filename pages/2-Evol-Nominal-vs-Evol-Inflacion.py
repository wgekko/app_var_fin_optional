import streamlit as st
import pandas as pd
import plotly.express as px
import base64
#from streamlit_extras.app_logo import add_logo

import warnings
warnings.simplefilter("ignore", category=FutureWarning)

#Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Evolucion nominal/inflacion", page_icon=":📊:", layout="wide")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


#----imagen en background y sider ---
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
    }
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background("images/fondodos.jpg")

st.sidebar.image("images/grafico1.gif", caption="Walter Gomez Financial Consultant")

df = pd.read_excel('assets/dolar_blue1.xlsx')

#option = st.selectbox(
#    'digite la variable a desplegar',
#    ('dolar_blue','dolar_ccl', 'dolar_mep', 'dolar_crypto', 'merval', 'pfijo')
#)

list_option = ['Dólar Blue', 'Dólar CCL', 'Dólar MEP', 'Dólar CRYPTO', 'Ind Merval', 'Plazo Fijo']
option = st.radio("Seleccione una opción : ", (list_option), horizontal=True )

st.write("---")
st.subheader(f"Evolución de {option} vs evolución de IPC/IPM (Mensual - nominal)")

# ---- DOLAR BLUE ----
if option == 'Dólar Blue':
    #st.write('el valor % de Plazo Fijo, están expresado en % mensual (periodo diario)- capitalización mensual')
    st.write("Se grafica con streamlit y con plotly debido a que se puede manipular el gráfico de alternativas distintas ")
    st.write("---")
    st.write("usando streamlit")
    st.line_chart(
        df,
        x='meses',
        y= ['IPC', 'IPM', option],
        color=["#FF0000", '#0000FF','#00FF00']
    )
    st.write("---")
    st.write("usando plotly")
    fig1= px.line(
        df,
        x='meses',
        y=['IPC', 'IPM', option],
        markers=True
    )
    st.plotly_chart(fig1, use_container_width=True)


# ---- DOLAR CCL ----
elif option == 'Dólar CCL':
    #st.write('el valor % de Plazo Fijo, están expresado en % mensual (periodo diario)- capitalización mensual')
    st.write("Se grafica con streamlit y con plotly debido a que se puede manipular el gráfico de alternativas distintas ")
    st.write("---")
    st.write("usando streamlit")
    st.line_chart(
        df,
        x='meses',
        y= ['IPC', 'IPM', option],
        color=["#FF0000", '#0000FF','#00FF00']
    )
    st.write("---")
    st.write("usando plotly")
    fig1= px.line(
        df,
        x='meses',
        y=['IPC', 'IPM', option],
        markers=True
    )
    st.plotly_chart(fig1, use_container_width=True)

# ---- DOLAR MEP ----
elif option == 'Dólar MEP':
    #st.write('el valor % de Plazo Fijo, están expresado en % mensual (periodo diario)- capitalización mensual')
    st.write("Se grafica con streamlit y con plotly debido a que se puede manipular el gráfico de alternativas distintas ")
    st.write("---")
    st.write("usando streamlit")
    st.line_chart(
        df,
        x='meses',
        y= ['IPC', 'IPM', option],
        color=["#FF0000", '#0000FF','#00FF00']
        )
    st.write("---")
    st.write("usando plotly")
    fig1= px.line(
        df,
        x='meses',
        y=['IPC', 'IPM', option],
        markers=True
        )
    st.plotly_chart(fig1, use_container_width=True)

# ---- DOLAR CRYPTO ----
elif option == 'Dólar CRYPTO':
    #st.write('el valor % de Plazo Fijo, están expresado en % mensual (periodo diario)- capitalización mensual')
    st.write("Se grafica con streamlit y con plotly debido a que se puede manipular el gráfico de alternativas distintas ")
    st.write("---")
    st.write("usando streamlit")
    st.line_chart(
        df,
        x='meses',
        y= ['IPC', 'IPM', option],
        color=["#FF0000", '#0000FF','#00FF00']
    )
    st.write("---")
    st.write("usando plotly")
    fig1= px.line(
        df,
        x='meses',
        y=['IPC', 'IPM', option],
        markers=True
    )
    st.plotly_chart(fig1, use_container_width=True)

# ---- MERVAL ----
elif option == 'Ind Merval':
    #st.write("Se grafica con streamlit y con plotly debido a que se puede manipular el gráfico de alternativas distintas ")
    st.write("---")
    st.write("usando streamlit")
    st.line_chart(
        df,
        x='meses',
        y= ['IPC', 'IPM', option],
        color=["#FF0000", '#0000FF','#00FF00']
    )
    st.write("---")
    st.write("usando plotly")
    fig1= px.line(
        df,
        x='meses',
        y=['IPC', 'IPM', option],
        markers=True
    )
    st.plotly_chart(fig1, use_container_width=True)

# ---- PFIJO ----
elif option == 'Plazo Fijo':
    st.write('el valor % de Plazo Fijo, están expresado en % mensual (periodo diario)- capitalización mensual')
    st.write("Se grafica con streamlit y con plotly debido a que se puede manipular el gráfico de alternativas distintas ")
    st.write("---")
    st.write("usando streamlit")
    st.line_chart(
        df,
        x='meses',
        y= ['IPC', 'IPM', option],
        color=["#FF0000", '#0000FF','#00FF00']
    )
    st.write("---")
    st.write("usando plotly")
    fig1= px.line(
        df,
        x='meses',
        y=['IPC', 'IPM', option],
        markers=True
    )
    st.plotly_chart(fig1, use_container_width=True)

else:
    st.write("Error, en la opción elegida ")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.write("&copy; - derechos reservados -  2023 -  Walter Gómez - FullStack Developer")
    st.write("##")
