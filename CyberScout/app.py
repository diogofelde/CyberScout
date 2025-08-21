pip install beautifulsoup4

python -c "from bs4 import BeautifulSoup; print('BeautifulSoup está funcionando!')"

import streamlit as st
import requests
from bs4 import BeautifulSoup
import tldextract

st.set_page_config(page_title="CyberScout", page_icon="🛡️")

st.title("CyberScout 🔍")
st.subheader("Análise de segurança cibernética para URLs suspeitas")

url = st.text_input("Digite a URL para análise:")

def verificar_url(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "Sem título"
        dominio = tldextract.extract(url).domain
        return {
            "status": "URL acessível",
            "domínio": dominio,
            "título": title
        }
    except Exception as e:
        return {
            "status": "URL inacessível ou suspeita",
            "erro": str(e)
        }

if url:
    resultado = verificar_url(url)
    st.write("🔎 Resultado da análise:")
    st.json(resultado)

