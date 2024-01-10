import streamlit as st
import pandas as pd
import base64
import yfinance as yf
import warnings
warnings.simplefilter("ignore", category=FutureWarning)

#-------------- logo de la pagina -----------------
#Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Analisis de Acciones", page_icon=":📊:", layout="wide")

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

st.sidebar.image("images/grafico6.gif", caption="Walter Gomez Financial Consultant")

#--------- mostramos mensaje de preparacion de datos ----------- 
st.write('Se está trabajando en el calculo de datos...')
st.write('proceso se demora unos segundos... ')    
st.write('---')   
  

# ---------------------- desarrollo de analisis de caida de acciones
años = 10
ruedas = 100  # La cantidad de ruedas para filtrar por volumen operado
cantidadAcciones = 40 # Las acciones de mayor volumen ultimas ruedas para mostrar 

ccl = pd.DataFrame()
adr = yf.download("YPF", period= str(años)+'Y' , interval='1d')['Adj Close']
local = yf.download("YPFD.BA", period=str(años)+'Y' , interval='1d')['Adj Close']
ccl = (local / adr).to_frame()
ccl.columns = ['CCL']

tickers = ['AGRO.BA','ALUA.BA','AUSO.BA','BBAR.BA','BHIP.BA','BMA.BA','BOLT.BA','BPAT.BA',
           'BYMA.BA','CADO.BA','CAPX.BA','CARC.BA','CECO2.BA','CELU.BA','CEPU.BA','CGPA2.BA','COME.BA',
           'CRES.BA','CTIO.BA','CVH.BA','DGCU2.BA','EDN.BA','FERR.BA','GAMI.BA','GARO.BA',
           'GCLA.BA','GGAL.BA','GRIM.BA','HARG.BA','HAVA.BA','INVJ.BA','IRS2W.BA',
           'IRSA.BA','LEDE.BA','LOMA.BA','LONG.BA','METR.BA','MIRG.BA','MOLA.BA','MOLI.BA','MORI.BA',
           'MTR.BA','OEST.BA','PAMP.BA','PATA.BA','POLL.BA','REGE.BA','RICH.BA','RIGO.BA','ROSE.BA','SAMI.BA','SEMI.BA','SUPV.BA',
           'TECO2.BA','TGNO4.BA','TGSU2.BA','TRAN.BA','TXAR.BA','VALO.BA','YPFD.BA']

data = yf.download(tickers, period=str(años)+'Y' , interval='1d')
vol = (data['Close']*data['Volume'] /1000000).rolling(ruedas).mean().tail(1).squeeze()
tickers = list(vol.sort_values(ascending=False).head(cantidadAcciones).index)

data = yf.download(tickers, period=str(años)+'Y' , interval='1d')['Adj Close'].abs()
dataCCL = data.div(ccl.CCL, axis=0)

fechasMax = dataCCL.idxmax()
preciosMax = dataCCL.max()
fechasMin = dataCCL.idxmin()
preciosHoy = dataCCL.tail(1).squeeze()
upside = ((preciosMax/preciosHoy-1)*100)
desdeMax = ((preciosHoy/preciosMax-1)*100)

tabla = pd.concat([fechasMax,fechasMin,preciosMax,preciosHoy,desdeMax,upside], axis=1)
tabla.columns = ['Fecha Px Max','Fecha Px Min','Px Max','Px Hoy','%DesdeMax','%HastaMax']
tabla = tabla.sort_values('%HastaMax', ascending=False).round(2)
# ---------------- cambio el formato de fecha a mostrar por consola 
tabla['Fecha Px Max'] = pd.to_datetime(tabla['Fecha Px Max'])
tabla['Fecha Px Max'] = tabla['Fecha Px Max'].dt.strftime("%d-%m-%Y")

tabla['Fecha Px Min'] = pd.to_datetime(tabla['Fecha Px Min'])
tabla['Fecha Px Min'] = tabla['Fecha Px Min'].dt.strftime("%d-%m-%Y")

    
# -------------- se muestran los datos de las tablas-----------------: 
st.write('proceso termando....!!!')     

st.write('Este modelo toma como referencia el tipo de cambio que surge de la accion YPF')
st.write('Entre mercado local y de EEUU, para poder establecer una metrica a valuar')
st.write('las acciones locales y medir su evolución de valor en dolares ')
st.write('desde 10 años hacia atrás hasta la fecha de hoy (también se pondera el volumen operado de los últimos 6 meses)')
with st.container():
    st.table(tabla)

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.write("&copy; - derechos reservados -  2023 -  Walter Gómez - FullStack Developer")
    st.write("##")
