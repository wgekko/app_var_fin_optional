import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import base64
from sklearn.model_selection import train_test_split
from sklearn import linear_model, tree, neighbors

import warnings
warnings.simplefilter("ignore", category=FutureWarning)

#Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Prediccion Rendimientos", page_icon=":📊:", layout="wide")

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


st.sidebar.image("images/grafico7.gif", caption="Walter Gomez Financial Consultant")

df = pd.read_excel('assets/dolar_blue3.xlsx')

#option = st.selectbox(
#    'digite la variable a desplegar',
#    ('dolar_blue','dolar_ccl', 'dolar_mep', 'dolar_crypto', 'merval', 'pfijo')
#)

list_option = ['Dólar Blue', 'Dólar CCL', 'Dólar MEP', 'Dólar CRYPTO', 'Ind Merval', 'Plazo Fijo']
option = st.radio("Seleccione una opción : ", (list_option), horizontal=True )

st.subheader(f"Gráficos de dispersión animado de : {option} ")
st.write("datos expresados en %, para medir la variación del valor en un periodo mensual(se aplica log natural)")
st.write("y para medir la volatilidad se aplica la desv. standar sobre la muestra de datos (periodo mensual)")

with st.container():
     # ---- DOLAR BLUE ----
    if option == 'Dólar Blue':
        df1 = pd.DataFrame(df)
        grafico = px.scatter(df1,
                                x=df1['blue_vol'],
                                y=df1['blue_rend'],
                                animation_frame= "meses",
                                animation_group="blue_rend",
                                size="blue_vol",
                                color='blue_rend',
                                hover_name='blue_rend',
                                size_max=45, range_x=[-5,40], range_y=[-20,50]

                              )
        st.plotly_chart(grafico, use_container_width=True)
    # ---- DOLAR CCL ----
    elif option == 'Dólar CCL':
        df1 = pd.DataFrame(df)
        grafico = px.scatter(df1,
                                x=df1['ccl_vol'],
                                y=df1['ccl_rend'],
                                animation_frame= "meses",
                                animation_group="ccl_rend",
                                size="ccl_vol",
                                color='ccl_rend',
                                hover_name='ccl_rend',
                                size_max=45, range_x=[-5,40], range_y=[-20,50]

                              )
        st.plotly_chart(grafico, use_container_width=True)

    # ---- DOLAR MEP ----
    elif option == 'Dólar MEP':
        df1 = pd.DataFrame(df)
        grafico = px.scatter(df1,
                                x=df1['mep_vol'],
                                y=df1['mep_rend'],
                                animation_frame= "meses",
                                animation_group="mep_rend",
                                size="mep_vol",
                                color='mep_rend',
                                hover_name='mep_rend',
                                size_max=45, range_x=[-5,40], range_y=[-20,50]

                              )
        st.plotly_chart(grafico, use_container_width=True)

    # ---- DOLAR CRYPTO ----
    elif option == 'Dólar CRYPTO':
        df1 = pd.DataFrame(df)
        grafico = px.scatter(df1,
                                x=df1['crypto_vol'],
                                y=df1['crypto_rend'],
                                animation_frame= "meses",
                                animation_group="crypto_rend",
                                size="crypto_vol",
                                color='crypto_rend',
                                hover_name='crypto_rend',
                                size_max=45, range_x=[-5,40], range_y=[-20,50]

                              )
        st.plotly_chart(grafico, use_container_width=True)

    # ---- DOLAR MERVAL ----
    elif option == 'Ind Merval':
        df1 = pd.DataFrame(df)
        grafico = px.scatter(df1,
                                x=df1['merval_vol'],
                                y=df1['merval_rend'],
                                animation_frame= "meses",
                                animation_group="merval_rend",
                                size="merval_vol",
                                color='merval_rend',
                                hover_name='merval_rend',
                                size_max=45, range_x=[-5,40], range_y=[-20,50]

                              )
        st.plotly_chart(grafico, use_container_width=True)

    # ---- DOLAR PLAZO FIJO ----
    elif option == 'Plazo Fijo':
        df1 = pd.DataFrame(df)
        grafico = px.scatter(df1,
                                x=df1['pfijo_vol'],
                                y=df1['pfijo_rend'],
                                animation_frame= "meses",
                                animation_group="pfijo_rend",
                                size="pfijo_vol",
                                color='pfijo_rend',
                                hover_name='pfijo_rend',
                                size_max=45, range_x=[-5,40], range_y=[-20,50]

                              )
        st.plotly_chart(grafico, use_container_width=True)
    else:
        st.write('Error, opcion no valida....!!!')

#st.write("datos expresados en %, para medir la variación del valor en un periodo mensual(se aplica log natural)")
#st.write("y para medir la volatilidad se aplica la desv. standar sobre la muestra de datos (periodo mensual)")
models = {'Regresión': linear_model.LinearRegression,
          'Arbol de Decisión': tree.DecisionTreeRegressor,
          'K-NN': neighbors.KNeighborsRegressor}

st.subheader(f"Gráficos de Predicción rendimientos de : {option} ")
option_list = ['Arbol de Decisión', 'Regresión', 'K-NN']
options = st.radio("Seleccione una opción : ", (option_list), horizontal=True )
st.subheader(f"Modelo desplegado de regresión  : {options} ")
st.write('x = % volatilidad, y = % rendimiento, linea = predicción  ')
with st.container():
    # ---- DOLAR BLUE ----
    if option == 'Dólar Blue':
        X = df['blue_vol'].values[:, None]
        X_train, X_test, y_train, y_test = train_test_split(
            X, df['blue_rend'], random_state=42)

        model = models[options]()
        model.fit(X_train, y_train)

        x_range = np.linspace(X.min(), X.max(), 800)
        y_range = model.predict(x_range.reshape(-1, 1))

        grafico1 = go.Figure([
            go.Scatter(x=X_train.squeeze(),
                       y=y_train,
                       name='train',
                       mode='markers'),
            go.Scatter(x=X_test.squeeze(),
                       y=y_test,
                       name='test',
                       mode='markers'),
            go.Scatter(x=x_range,
                       y=y_range,
                       name='prediction'),

        ])
        st.plotly_chart(grafico1,use_container_width=True)
    # ---- DOLAR CCL ----
    elif option == 'Dólar CCL':
        X = df['ccl_vol'].values[:, None]
        X_train, X_test, y_train, y_test = train_test_split(
            X, df['ccl_rend'], random_state=42)

        model = models[options]()
        model.fit(X_train, y_train)

        x_range = np.linspace(X.min(), X.max(), 800)
        y_range = model.predict(x_range.reshape(-1, 1))

        grafico1 = go.Figure([
            go.Scatter(x=X_train.squeeze(),
                       y=y_train,
                       name='train',
                       mode='markers'),
            go.Scatter(x=X_test.squeeze(),
                       y=y_test,
                       name='test',
                       mode='markers'),
            go.Scatter(x=x_range,
                       y=y_range,
                       name='prediction'),

        ])
        st.plotly_chart(grafico1,use_container_width=True)

    # ---- DOLAR MEP ----
    elif option == 'Dólar MEP':
        X = df['mep_vol'].values[:, None]
        X_train, X_test, y_train, y_test = train_test_split(
            X, df['mep_rend'], random_state=42)

        model = models[options]()
        model.fit(X_train, y_train)

        x_range = np.linspace(X.min(), X.max(), 800)
        y_range = model.predict(x_range.reshape(-1, 1))

        grafico1 = go.Figure([
            go.Scatter(x=X_train.squeeze(),
                       y=y_train,
                       name='train',
                       mode='markers'),
            go.Scatter(x=X_test.squeeze(),
                       y=y_test,
                       name='test',
                       mode='markers'),
            go.Scatter(x=x_range,
                       y=y_range,
                       name='prediction'),

        ])
        st.plotly_chart(grafico1,use_container_width=True)

    # ---- DOLAR CRYPTO ----
    elif option == 'Dólar CRYPTO':
        X = df['crypto_vol'].values[:, None]
        X_train, X_test, y_train, y_test = train_test_split(
            X, df['crypto_rend'], random_state=42)

        model = models[options]()
        model.fit(X_train, y_train)

        x_range = np.linspace(X.min(), X.max(), 800)
        y_range = model.predict(x_range.reshape(-1, 1))

        grafico1 = go.Figure([
            go.Scatter(x=X_train.squeeze(),
                       y=y_train,
                       name='train',
                       mode='markers'),
            go.Scatter(x=X_test.squeeze(),
                       y=y_test,
                       name='test',
                       mode='markers'),
            go.Scatter(x=x_range,
                       y=y_range,
                       name='prediction'),

        ])
        st.plotly_chart(grafico1,use_container_width=True)

    # ---- DOLAR MERVAL ----
    elif option == 'Ind Merval':
        X = df['merval_vol'].values[:, None]
        X_train, X_test, y_train, y_test = train_test_split(
            X, df['merval_rend'], random_state=42)

        model = models[options]()
        model.fit(X_train, y_train)

        x_range = np.linspace(X.min(), X.max(), 800)
        y_range = model.predict(x_range.reshape(-1, 1))

        grafico1 = go.Figure([
            go.Scatter(x=X_train.squeeze(),
                       y=y_train,
                       name='train',
                       mode='markers'),
            go.Scatter(x=X_test.squeeze(),
                       y=y_test,
                       name='test',
                       mode='markers'),
            go.Scatter(x=x_range,
                       y=y_range,
                       name='prediction'),

        ])
        st.plotly_chart(grafico1,use_container_width=True)

    # ---- DOLAR PFIJO ----
    elif option == 'Plazo Fijo':
        X = df['pfijo_vol'].values[:, None]
        X_train, X_test, y_train, y_test = train_test_split(
            X, df['pfijo_rend'], random_state=42)

        model = models[options]()
        model.fit(X_train, y_train)

        x_range = np.linspace(X.min(), X.max(), 800)
        y_range = model.predict(x_range.reshape(-1, 1))

        grafico1 = go.Figure([
            go.Scatter(x=X_train.squeeze(),
                       y=y_train,
                       name='train',
                       mode='markers'),
            go.Scatter(x=X_test.squeeze(),
                       y=y_test,
                       name='test',
                       mode='markers'),
            go.Scatter(x=x_range,
                       y=y_range,
                       name='prediction'),

        ])
        st.plotly_chart(grafico1,use_container_width=True)

    else:
        st.write('Error, no es una opción valida')


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.write("&copy; - derechos reservados -  2023 -  Walter Gómez - FullStack Developer")
    st.write("##")
