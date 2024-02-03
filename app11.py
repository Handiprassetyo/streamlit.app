import pandas as pd
import plotly.express as px
import streamlit as st
import base64

st.set_page_config(page_title="Uas Kelompok",
                 layout= "wide",
                )
df = pd.read_csv('C:/Users/20200/Downloads/Documents/DATA PRODUK EDIFIER TRAINING (2).csv', sep=';')


def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


csv = convert_df(df)

st.dataframe(df)


st.sidebar.header("Filter:")
nama_produk = st.sidebar.multiselect(
    "Select the nama_produk:",
     options=df["nama_produk"].unique(),
     default=df["nama_produk"].unique()
    )
#------Ganti tanggal masuk-----#
tanggal_masuk = st.sidebar.multiselect(
    "Select the tanggal masuk:",
     options=df["tanggal_masuk"].unique(),
     default=df["tanggal_masuk"].unique()
    )
#--------ganti kuantitas terjual------#
kuantitas_terjual = st.sidebar.multiselect(
    "Select the kuantitas terjual:",
     options=df["kuantitas_terjual"].unique(),
     default=df["kuantitas_terjual"].unique()
    )

df_selection=df.query(
  "nama_produk== @nama_produk & tanggal_masuk== @tanggal_masuk & kuantitas_terjual == @kuantitas_terjual"
)


st.dataframe(df_selection)




st.title( "Uas Kelompok")
st.markdown("##")