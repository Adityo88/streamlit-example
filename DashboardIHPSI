import streamlit as st
import pandas as pd
import plotly.express as px

def read_data():
    df = pd.read_excel("Data/Tindak Lanjut.xlsx", sheet_name='IHPSI2021')
    return df

def main():
    hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    st.sidebar.header('Dashboard Temuan dan Tindak Lanjut Kementerian/Lembaga IHPS I 2021')
    df = read_data()

    Entitas = st.sidebar.multiselect(
        "Pilih Kementerian/Lembaga:",
        options=df["Entitas"].unique(),
        default=df["Entitas"].unique().tolist()
    )
    Periode = st.sidebar.multiselect(
        "Pilih Periode Pemeriksaan:",
        options=df["Periode"].unique(),
        default=df["Periode"].unique().tolist()
    )
    df_selection = df.query(
        "Entitas == @Entitas & Periode == @Periode"
    )
    st.write(df_selection)

    Pilih_Tahun = df["Periode"].unique().tolist()
    Tahun = st.selectbox("Pilih Periode", Pilih_Tahun, 0)
    df_selection = df[df['Periode']== Tahun]

    Pilih_Entitas = df["Entitas"].unique().tolist()
    Entitas = st.selectbox("Pilih Entitas", Pilih_Entitas, 0)
    df_selection = df[df['Entitas']== Entitas]

    fig= px.bar(df_selection, x='Entitas',y='Jml Temuan')
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
