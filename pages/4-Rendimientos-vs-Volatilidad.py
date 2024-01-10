import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import numpy as np
import base64

import warnings
warnings.simplefilter("ignore", category=FutureWarning)

#Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Rendimientos/Volatilidad", page_icon=":📊:", layout="wide")

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

set_background("images/fondo_muro_1.jpg")


st.sidebar.image("images/grafico4.gif", caption="Walter Gomez Financial Consultant")

df = pd.read_excel('assets/dolar_blue3.xlsx')

#option = st.selectbox(
#    'digite la variable a desplegar',
#    ('dolar_blue','dolar_ccl', 'dolar_mep', 'dolar_crypto', 'merval', 'pfijo')
#)

list_option = ['Dólar Blue', 'Dólar CCL', 'Dólar MEP', 'Dólar CRYPTO', 'Ind Merval', 'Plazo Fijo']
option = st.radio("Seleccione una opción : ", (list_option), horizontal=True )



st.subheader(f"Gráficos de dispersión de : {option} ")
st.write("datos expresados en %, para medir la variación del valor en un periodo mensual(se aplica log natural)")
st.write("y para medir la volatilidad se aplica la desv. standar sobre la muestra de datos (periodo mensual)")

with st.container():
    st.subheader("Gráfico de Rendimiento/Volatilidad(mensual) con streamlit")
    # ---- DOLAR BLUE ----
    if option == 'Dólar Blue':
        grafico = alt.Chart(df).mark_circle().encode(
            x="blue_vol",
            y="blue_rend",
            size="blue_rend",
            color=alt.value('yellow')
            )
        st.altair_chart(grafico, use_container_width=True)

        st.subheader("Gráfico de Histograma de Rendimiento (mensual)")
        grafico2=alt.Chart(df).mark_bar(color="green").encode(
            alt.X("blue_rend", bin=True),
            y='count()',
        )
        st.altair_chart(grafico2, use_container_width=True)

        st.subheader("Gráfico de ajuste polinómico con transformación de regresión (mensual)")
        x = df["blue_vol"]
        y = df["blue_rend"]
        source = pd.DataFrame({"x": x, "y": y})
        # Define the degree of the polynomial fits
        degree_list = [1, 3, 5]

        base = alt.Chart(source).mark_circle(color="yellow").encode(
            alt.X("x"),
            alt.Y("y")
        )

        grafico3 = [
            base.transform_regression(
                "x", "y", method="poly", order=order, as_=["x", str(order)]
            )
            .mark_line()
            .transform_fold([str(order)], as_=["degree", "y"])
            .encode(alt.Color("degree:N"))
            for order in degree_list
        ]
        alt.layer(base, *grafico3)
        st.altair_chart(alt.layer(base, *grafico3),use_container_width=True)

      # ---- DOLAR CCL ----
    elif option == 'Dólar CCL':
        grafico = alt.Chart(df).mark_circle().encode(
            x="ccl_vol",
            y="ccl_rend",
            size="ccl_rend",
            color=alt.value('yellow')
            )
        st.altair_chart(grafico, use_container_width=True)

        st.subheader("Gráfico de Histograma de Rendimiento (mensual)")
        grafico2=alt.Chart(df).mark_bar(color="green").encode(
            alt.X("ccl_rend", bin=True),
            y='count()',
        )
        st.altair_chart(grafico2, use_container_width=True)

        st.subheader("Gráfico de ajuste polinómico con transformación de regresión (mensual)")
        x = df["ccl_vol"]
        y = df["ccl_rend"]
        source = pd.DataFrame({"x": x, "y": y})
        # Define the degree of the polynomial fits
        degree_list = [1, 3, 5]

        base = alt.Chart(source).mark_circle(color="yellow").encode(
            alt.X("x"),
            alt.Y("y")
        )
        grafico3 = [
            base.transform_regression(
                "x", "y", method="poly", order=order, as_=["x", str(order)]
            )
            .mark_line()
            .transform_fold([str(order)], as_=["degree", "y"])
            .encode(alt.Color("degree:N"))
            for order in degree_list
        ]
        alt.layer(base, *grafico3)
        st.altair_chart(alt.layer(base, *grafico3),use_container_width=True)

      # ---- DOLAR MEP ----
    elif option == 'Dólar MEP':
        grafico = alt.Chart(df).mark_circle().encode(
            x="mep_vol",
            y="mep_rend",
            size="mep_rend",
            color=alt.value('yellow')
            )
        st.altair_chart(grafico, use_container_width=True)

        st.subheader("Gráfico de Histograma de Rendimiento (mensual)")
        grafico2=alt.Chart(df).mark_bar(color="green").encode(
            alt.X("mep_rend", bin=True),
            y='count()',
        )
        st.altair_chart(grafico2, use_container_width=True)

        st.subheader("Gráfico de ajuste polinómico con transformación de regresión (mensual)")
        x = df["mep_vol"]
        y = df["mep_rend"]
        source = pd.DataFrame({"x": x, "y": y})
        # Define the degree of the polynomial fits
        degree_list = [1, 3, 5]

        base = alt.Chart(source).mark_circle(color="yellow").encode(
            alt.X("x"),
            alt.Y("y")
        )

        grafico3 = [
            base.transform_regression(
                "x", "y", method="poly", order=order, as_=["x", str(order)]
            )
            .mark_line()
            .transform_fold([str(order)], as_=["degree", "y"])
            .encode(alt.Color("degree:N"))
            for order in degree_list
        ]
        alt.layer(base, *grafico3)
        st.altair_chart(alt.layer(base, *grafico3),use_container_width=True)
    # ---- DOLAR CRYPTO ----
    elif option == 'Dólar CRYPTO':
        grafico = alt.Chart(df).mark_circle().encode(
            x="crypto_vol",
            y="crypto_rend",
            size="crypto_rend",
            color=alt.value('yellow')
            )
        st.altair_chart(grafico, use_container_width=True)

        st.subheader("Gráfico de Histograma de Rendimiento (mensual)")
        grafico2=alt.Chart(df).mark_bar(color="green").encode(
            alt.X("crypto_rend", bin=True),
            y='count()',
        )
        st.altair_chart(grafico2, use_container_width=True)

        st.subheader("Gráfico de ajuste polinómico con transformación de regresión (mensual)")
        x = df["crypto_vol"]
        y = df["crypto_rend"]
        source = pd.DataFrame({"x": x, "y": y})
        # Define the degree of the polynomial fits
        degree_list = [1, 3, 5]

        base = alt.Chart(source).mark_circle(color="yellow").encode(
            alt.X("x"),
            alt.Y("y")
        )

        grafico3 = [
            base.transform_regression(
                "x", "y", method="poly", order=order, as_=["x", str(order)]
            )
            .mark_line()
            .transform_fold([str(order)], as_=["degree", "y"])
            .encode(alt.Color("degree:N"))
            for order in degree_list
        ]
        alt.layer(base, *grafico3)
        st.altair_chart(alt.layer(base, *grafico3),use_container_width=True)
    # ---- MERVAL ----
    elif option == 'Ind Merval':
        grafico = alt.Chart(df).mark_circle().encode(
            x="merval_vol",
            y="merval_rend",
            size="merval_rend",
            color=alt.value('yellow')
            )
        st.altair_chart(grafico, use_container_width=True)

        st.subheader("Gráfico de Histograma de Rendimiento (mensual)")
        grafico2=alt.Chart(df).mark_bar(color="green").encode(
            alt.X("merval_rend", bin=True),
            y='count()',
        )
        st.altair_chart(grafico2, use_container_width=True)

        st.subheader("Gráfico de ajuste polinómico con transformación de regresión (mensual)")
        x = df["merval_vol"]
        y = df["merval_rend"]
        source = pd.DataFrame({"x": x, "y": y})
        # Define the degree of the polynomial fits
        degree_list = [1, 3, 5]

        base = alt.Chart(source).mark_circle(color="yellow").encode(
            alt.X("x"),
            alt.Y("y")
        )

        grafico3 = [
            base.transform_regression(
                "x", "y", method="poly", order=order, as_=["x", str(order)]
            )
            .mark_line()
            .transform_fold([str(order)], as_=["degree", "y"])
            .encode(alt.Color("degree:N"))
            for order in degree_list
        ]
        alt.layer(base, *grafico3)
        st.altair_chart(alt.layer(base, *grafico3),use_container_width=True)
    # ---- PLAZO FIJO ----
    elif option == 'Plazo Fijo':
        grafico = alt.Chart(df).mark_circle().encode(
            x="pfijo_vol",
            y="pfijo_rend",
            size="pfijo_rend",
            color=alt.value('yellow')
            )
        st.altair_chart(grafico, use_container_width=True)

        st.subheader("Gráfico de Histograma de Rendimiento (mensual)")
        grafico2=alt.Chart(df).mark_bar(color="green").encode(
            alt.X("pfijo_rend", bin=True),
            y='count()',
        )
        st.altair_chart(grafico2, use_container_width=True)

        st.subheader("Gráfico de ajuste polinómico con transformación de regresión (mensual)")
        x = df["pfijo_vol"]
        y = df["pfijo_rend"]
        source = pd.DataFrame({"x": x, "y": y})
        # Define the degree of the polynomial fits
        degree_list = [1, 3, 5]

        base = alt.Chart(source).mark_circle(color="yellow").encode(
            alt.X("x"),
            alt.Y("y")
        )

        grafico3 = [
            base.transform_regression(
                "x", "y", method="poly", order=order, as_=["x", str(order)]
            )
            .mark_line()
            .transform_fold([str(order)], as_=["degree", "y"])
            .encode(alt.Color("degree:N"))
            for order in degree_list
        ]
        alt.layer(base, *grafico3)
        st.altair_chart(alt.layer(base, *grafico3),use_container_width=True)
    else:
       st.write("Error, verifique la opción seleccinada")

with st.container():
    st.subheader(" Gráfico de Rendimiento/Volatilidad(mensual) con plotly")
    # ---- DOLAR BLUE ----
    if option == 'Dólar Blue':
        fig = px.scatter(
                df,
                x="blue_vol",
                y="blue_rend",
                color="blue_rend",
                trendline='ols', trendline_color_override='darkblue',
                color_continuous_scale="reds"
            )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

        fig1 = px.scatter(df, x = "blue_vol", y = "blue_rend",
                    marginal_x = "histogram", marginal_y = "histogram",
                    trendline='ols', trendline_options=dict(log_x=True),
                    trendline_color_override='darkblue',
                    )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.write('se grafica el log a la regresion')
                st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig1, theme=None, use_container_width=True)

    # ---- DOLAR CCL ----
    elif option == 'Dólar CCL':
        fig = px.scatter(
                df,
                x="ccl_vol",
                y="ccl_rend",
                color="ccl_rend",
                trendline='ols', trendline_color_override='darkblue',
                color_continuous_scale="reds"
            )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

        fig1 = px.scatter(df, x = "ccl_vol", y = "ccl_rend",
                    marginal_x = "histogram", marginal_y = "histogram",
                    trendline='ols', trendline_options=dict(log_x=True),
                    trendline_color_override='darkblue',
                    )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.write('se grafica el log a la regresion')
                st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig1, theme=None, use_container_width=True)
    # ---- DOLAR MEP ----
    elif option == 'Dólar MEP':
        fig = px.scatter(
                df,
                x="mep_vol",
                y="mep_rend",
                color="mep_rend",
                trendline='ols', trendline_color_override='darkblue',
                color_continuous_scale="reds"
            )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

        fig1 = px.scatter(df, x = "mep_vol", y = "mep_rend",
                    marginal_x = "histogram", marginal_y = "histogram",
                    trendline='ols', trendline_options=dict(log_x=True),
                    trendline_color_override='darkblue',
                    )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.write('se grafica el log a la regresion')
                st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig1, theme=None, use_container_width=True)

    # ---- DOLAR CRYPTO ----
    elif option == 'Dólar CRYPTO':
        fig = px.scatter(
                df,
                x="crypto_vol",
                y="crypto_rend",
                color="crypto_rend",
                trendline='ols', trendline_color_override='darkblue',
                color_continuous_scale="reds"
            )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

        fig1 = px.scatter(df, x = "crypto_vol", y = "crypto_rend",
                    marginal_x = "histogram", marginal_y = "histogram",
                    trendline='ols', trendline_options=dict(log_x=True),
                    trendline_color_override='darkblue',
                    )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.write('se grafica el log a la regresion')
                st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig1, theme=None, use_container_width=True)

    # ---- MERVAL ----
    elif option == 'Ind Merval':
        fig = px.scatter(
                df,
                x="merval_vol",
                y="merval_rend",
                color="merval_rend",
                trendline='ols', trendline_color_override='darkblue',
                color_continuous_scale="reds"
            )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

        fig1 = px.scatter(df, x = "merval_vol", y = "merval_rend",
                    marginal_x = "histogram", marginal_y = "histogram",
                    trendline='ols', trendline_options=dict(log_x=True),
                    trendline_color_override='darkblue',
                    )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.write('se grafica el log a la regresion')
                st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig1, theme=None, use_container_width=True)

    # ---- PLAZO FIJO ----
    elif option == 'Plazo Fijo':
        fig = px.scatter(
                df,
                x="pfijo_vol",
                y="pfijo_rend",
                color="pfijo_rend",
                trendline='ols', trendline_color_override='darkblue',
                color_continuous_scale="reds"
            )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

        fig1 = px.scatter(df, x = "pfijo_vol", y = "pfijo_rend",
                    marginal_x = "histogram", marginal_y = "histogram",
                    trendline='ols',
                    trendline_color_override='darkblue',
                    )

        tab1, tab2 = st.tabs(["fondo transparente", "fondo color intenso"])
        with tab1:
                st.write('se grafica  la regresion')
                st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
        with tab2:
                st.plotly_chart(fig1, theme=None, use_container_width=True)

    else:
        st.write("Error, verifique la opción seleccinada")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.write("&copy; - derechos reservados -  2023 -  Walter Gómez - FullStack Developer")
    st.write("##")
