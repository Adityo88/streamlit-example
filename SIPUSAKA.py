import streamlit as st 
import pandas as pd 
import numpy as np 
import logging
import plotly.express as px 
from TinjutIHPS import run_TinjutIHPS

st.set_page_config(
    page_title="SIPUSAKA",
    page_icon="PUSKAJIAKN-01.png",
    layout="wide"
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter("%(levelname)s %(asctime)s.%(msecs)03d -%(message)s")

# File
file_handler = logging.FileHandler('activity.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def main():
    st.title("Sistem Informasi PuskajiAKN")
    menu = ["Beranda","Tindak Lanjut IHPS","APBN","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Beranda":
        st.subheader("Beranda")
        
    elif choice == "Tindak Lanjut IHPS":
        run_TinjutIHPS()
    
    elif choice == "APBN":
        st.subheader("APBN")
    
    else:
        st.subheader("About")

if __name__ == '__main__':
    main()
