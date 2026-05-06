import streamlit as st
import pandas as pd
from datetime import time, date

# Import du dataframe
link = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
dftaxi = pd.read_csv(link)

liste_pickup_zone = dftaxi["pickup_borough"].unique()

# Apparence du site
st.title("Bienvenue sur le site web de Clacla")

# Un menu déroulant où l'utilisateur peut sélectionner une seule option.
lieu = st.selectbox("Ou souhaitez vous être récupéré ?", liste_pickup_zone) 
st.write('___')
st.write("Tu as choisie :", lieu)
if lieu == "Manhattan":
    st.image("https://www.civitatis.com/f/estados-unidos/nueva-york/tour-manhattan-589x392.jpg")
elif lieu == "Queens":
    st.image("https://images.ctfassets.net/1aemqu6a6t65/6SEfpIJVEjWwp4kH4EqW2G/6e0dbff965675f944928c7511e711567/Sunnyside-Queens-NYC-Photo-VincentTullo-40.jpg")
elif lieu == "Bronx":
    st.image("https://thegoodlife.fr/wp-content/thumbnails/uploads/sites/2/2016/03/TGL-P-022-188-V-H-06-tt-width-2000-height-1282-fill-0-crop-0-bgcolor-eeeeee.jpg")
elif lieu == "Brooklyn":
    st.image("https://static.wixstatic.com/media/108ff4_f10a7205eb0546dea88e529a8474f932~mv2.jpg/v1/fill/w_980,h_676,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/108ff4_f10a7205eb0546dea88e529a8474f932~mv2.jpg")
else:
    st.write("Choisie un lieu de récupération")
    st.image("https://novaumc.org/wp-content/uploads/2019/10/stay.png")