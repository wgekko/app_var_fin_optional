import requests
import streamlit as st
from streamlit_lottie import st_lottie
import base64
import warnings
warnings.simplefilter("ignore", category=FutureWarning)

#Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Analisis Dólar", page_icon=":📊:", layout="wide")

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


st.sidebar.image("images/grafico5.gif", caption="Walter Gomez Financial Consultant")

st.markdown(
    '''
    <style>
    sidebar {
        background-image: linear-gradiant('images/imge-slide.jpg'));
    }
    </style>
    ''',
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
        st.title("Análisis de Dólar Blue-MEP-CCL")
        st.subheader("De desarrolla los siguientes temas :")
        #st.write("#")
        st.subheader(
            "Evolución de la brecha cambiaria, probabilidad de suba o baja, proyecciones."
        )
        st.write("Fuente: BCRA, BYMA, ambito financiero.")
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
        st.subheader("En la barra lateral accedemos")
        st.subheader("- Análisis de Brechas de Dolar")
        st.subheader("- Análisis de Probabilidades del Dolar")
        st.subheader("- Análsis de CCL")
        st.subheader("- Predicción de tipo de cambio")
        st.subheader("- Análisis de Acciones(en U$D)")
    with right_column:
        st.write("#")
        #st.write("#")
        st_lottie(lottie_coding, height=300, key="coding")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.write("&copy; - derechos reservados -  2023 -  Walter Gómez - FullStack Developer")
    st.write("##")


