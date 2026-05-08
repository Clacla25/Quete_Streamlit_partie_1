import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Liste de tout les datasets
liste_dataset = sns.get_dataset_names()

# Titre du site
st.title("Manipulation de données et création de graphiques")

# Un menu déroulant où l'utilisateur peut sélectionner une seule option.
choix = st.selectbox("Quel dataset veux tu utiliser ?", liste_dataset) 
st.write('___')
st.write("Tu as choisie :", choix)

# Téléchargement du dataset choisie
dataset = sns.load_dataset(choix)
# Affiche le dataset
st.dataframe(dataset)


# Liste de toutes les datasets
liste_colonne = dataset.columns
# Un menu déroulant
choix_colonneX = st.selectbox("Choisissez la colonne X ?", liste_colonne) 
st.write('___')

# Un menu déroulant
choix_colonneY = st.selectbox("Choisissez la colonne Y ?", liste_colonne) 
st.write('___')


# Liste des graph /!\ important de ne pas mettre les () pour les graph, sinon cela appel la fonction direct 
# ce qui crée un bug.
graph = {"Area chart" : st.area_chart,
         "Bar chart" : st.bar_chart,
         "Line chart" : st.line_chart,
         "Scatter chart" : st.scatter_chart}
 
# Un menu déroulant
choix_graph = st.selectbox("Choisissez un graphique ?", graph.keys()) 
st.write('___')

# Graphique
graph[choix_graph](dataset, x=choix_colonneX, y=choix_colonneY)

# Ajout d'une case à cocher
agree = st.checkbox("Afficher la matrice de corrélation")
if agree :
    try :
        # Affichage le heatmap de corrélation
        fig, ax = plt.subplots()
        sns.heatmap(data=dataset[[choix_colonneX, choix_colonneY]].select_dtypes("number").corr(), 
                    cmap=sns.color_palette('coolwarm', as_cmap=True), center=0, ax=ax)
        st.pyplot(fig)
    except ValueError :
        st.error("❌ Impossible d'afficher la corrélation : Pour cela les colonnes doivent être remplie uniquement de type numérique, choisie une autre colonne")
    