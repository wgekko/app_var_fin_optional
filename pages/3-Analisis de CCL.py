import streamlit as st
import pandas as pd
import plotly.express as px
import base64
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter("ignore", category=FutureWarning)
#-------------- logo de la pagina -----------------
#Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Analisis de CCL", page_icon=":📊:", layout="wide")

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

set_background("images/fondo_muro.jpg")

st.sidebar.image("images/grafico3.gif", caption="Walter Gomez Financial Consultant")

#----------- Prespectivas de suba del CCL------------------------
tickers1 =['CEPU','CEPU.BA','GGAL','GGAL.BA','YPF','YPFD.BA','PAM','PAMP.BA']
dato = yf.download(tickers1, auto_adjust=True, start='2020-01-01')['Close']

ccl = dato['YPFD.BA']/dato['YPF']
ccl += dato['CEPU.BA']/dato['CEPU'] * 10
ccl += dato['GGAL.BA']/dato['GGAL'] * 10
ccl += dato['PAMP.BA']/dato['PAM'] * 25
ccl /= 4

ruedas = 60
subas_fw = ccl.pct_change(ruedas)*100 

values = [5,10,15,20,25,30]
targets = ((1 + np.array(values)/100)*ccl.iloc[-1]).round(2)
st.container()
st.subheader('Análisis de Probabilidades de suba en el dólar CCL')
st.markdown(f'Se calcula para {ruedas} ruedas bursátiles, de las acciones con cotización mercado local')
st.markdown('CEPU, GGAL, PAMP, YPF, como referencia y con relación a sus cotizaciones en dólares en el mercado de EEUU')
with st.container():    
    for z in range(len(values)):    
        sup_z = len(subas_fw.loc[subas_fw > values[z] ])/len(subas_fw)
        st.markdown(f'Suba mayores a : {values[z]}% - objetivo (${targets[z]}): {round(sup_z*100,1)}%')

st.write("---")
#----------- Prespectivas de baja del CCL------------------------
tickers =['CEPU','CEPU.BA','GGAL','GGAL.BA','YPF','YPFD.BA','PAM','PAMP.BA']
data = yf.download(tickers, auto_adjust=True, start='2020-01-01')['Close']

ccl = data['YPFD.BA']/data['YPF']
ccl += data ['CEPU.BA']/data['CEPU'] * 10
ccl += data['GGAL.BA']/data['GGAL'] * 10
ccl += data['PAMP.BA']/data['PAM'] * 25
ccl /= 4
ccl_max_h = ccl.cummax()
ccl_dd = ((ccl/ccl_max_h-1)*100).dropna().rolling(60).mean()

values = [-10,-15,-20,-25]
targets = ((1 + np.array(values)/100)*ccl.iloc[-1]).round(2)

st.subheader('Análisis de Probabilidades de bajas en el dólar CCL')
with st.container():
    for z in range(len(values)):   
        sub_z = len(ccl_dd.loc[ccl_dd < values[z] ])/len(ccl_dd)
        st.markdown(f'Baja  mayor a : {-values[z]}% -objetivo  (${targets[z]}) : {round(sub_z*100,1)} %')


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.write("&copy; - derechos reservados -  2023 -  Walter Gómez - FullStack Developer")
    st.write("##")
