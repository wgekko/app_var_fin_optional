import requests
import streamlit as st
from streamlit_lottie import st_lottie
import base64
import warnings
warnings.simplefilter("ignore", category=FutureWarning)


#Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Financial Analysis", page_icon=":📊:", layout="wide")

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

# side bar--- y redimencionar la imagen
#img = cv2.imread("images/analisisfin.png")
#scale_porcent = 30
#width = int(img.shape[1]*scale_porcent/100)
#heigth = int(img.shape[0]*scale_porcent/100)
#dim =(width, heigth)
#resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

#st.sidebar.image("images/analisisfin.png", caption="Walter Gomez Financial Consultant")

st.sidebar.image("images/grafico5.gif", caption="Walter Gomez Financial Consultant")

st.markdown(
    """
<style>
sidebar  {
    background-image: ('images/sider.jpg'));
}
</style>
""",
    unsafe_allow_html=True,
)

# despliegue de imagen lottier
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# despliegue de archivo gif
file_ = open("images/data.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- Carga de componentes ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# ---- cabecera de la pagina  ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Análisis de Variables Financieras 📈")
        st.subheader("variables para el análisis son :")
        #st.write("#")
        st.subheader(
            "Dólar Blue, Dólar CCL, Dólar Mep, Dólar Crypto, Indice Merval, Tasa Plazo Fijo, Inflación(ind. de precio minorista/mayorista)."
        )
        st.write("Fuente: BCRA, BYMA, ambito financiero ." )
    with right_column:
        #st.write("#")
        #st.write("#")
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" width="500"  alt="analisis gif">',
            unsafe_allow_html=True,
        )

# ---- Descripcion de la pagina----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        #st.subheader("Contenido de la página")
        #st.write("##")
        #st.write("##")
        st.subheader("En la barra lateral accedemos :" )
        st.subheader("- Gráficos de Evolución Variables (diario)")
        st.subheader("- Gráficos Evol. Nominal vs Evol. inflación (mensual)")
        st.subheader("- Gráficos de Variables Deflactadas (mensual)")
        st.subheader("- Gráficos de rentabilidad y volatilidad (mensual)")
        st.subheader("- Gráficos de predicción de rentabilidad-animaciones de rendimientos (mensual)")
    with right_column:
        st.write("#")
        #st.write("#")
        st_lottie(lottie_coding, height=300, key="coding")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.write("&copy; - derechos reservados -  2023 -  Walter Gómez - FullStack Developer")
    st.write("##")


