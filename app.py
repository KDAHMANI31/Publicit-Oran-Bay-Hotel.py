import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Publicité Oran Bay Hotel *****", page_icon="🎬", layout="wide"
)

# Titre Principal
st.title("🎬 Campagne Publicitaire — Oran Bay Hotel *****")
st.subheader("Script de vidéo promotionnelle (Format 45 secondes)")

st.markdown("---")

# Présentation synthétique
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Format", value="Reels / TV / Web")
with col2:
    st.metric(label="Durée Cible", value="45 secondes")
with col3:
    st.metric(label="Style Sonore", value="Lounge / Électro Chic")

st.markdown("---")

# Affichage du script étape par étape
st.header("📋 Découpage Scène par Scène")

with st.expander("🔹 Scene 1 : Introduction & Baie d'Oran (00:00 - 00:07)", expanded=True):
    st.markdown("""
    * **Visuel :** Plan au drone de la baie d'Oran au lever du soleil, révélant la façade moderne en verre bleu du gratte-ciel de l'Oran Bay.
    * **Voix-Off :** *« Au cœur de la majestueuse baie d'Oran, là où le ciel rencontre la Méditerranée… découvrez un écran de raffinement et d'élégance absolue. »*
    * **Texte Écran :** `Bienvenue à l'Oran Bay Hotel *****`
    """)

with st.expander("🔹 Scene 2 : Suites & Confort Panoramique (00:07 - 00:15)"):
    st.markdown("""
    * **Visuel :** Ouverture automatique des rideaux d'une suite exécutive, dévoilant la vue panoramique sur la mer. Un client savoure son café.
    * **Voix-Off :** *« Éveillez vos sens dans des suites d'exception, baignées de lumière, offrant une vue panoramique sur l'horizon marine. »*
    * **Texte Écran :** `Des Espaces Pensés Pour Votre Confort`
    """)

with st.expander("🔹 Scene 3 : Gastronomie & Restauration (00:15 - 00:25)"):
    st.markdown("""
    * **Visuel :** Plans dynamiques et élégants : le chef dressant une assiette gastronomique, puis un cocktail servi au bar panoramique.
    * **Voix-Off :** *« Laissez-vous séduire par une gastronomie raffinée, où chaque création de nos chefs est une véritable invitation au voyage. »*
    * **Texte Écran :** `Une Expérience Gastronomique Unique`
    """)

with st.expander("🔹 Scene 4 : Piscine & Bien-Être (00:25 - 00:35)"):
    st.markdown("""
    * **Visuel :** Plan fluide sur la piscine extérieure ensoleillée, suivi d'une transition vers le spa et le centre de remise en forme.
    * **Voix-Off :** *« Ressourcez-vous au bord de nos espaces aquatiques ou profitez d'un moment de sérénité au sein de notre spa d'exception. »*
    * **Texte Écran :** `Sérénité & Détente Absolue`
    """)

with st.expander("🔹 Scene 5 : Outro & Appel à l'Action (00:35 - 00:45)"):
    st.markdown("""
    * **Visuel :** Vue nocturne spectaculaire du bâtiment illuminé. Affichage du logo officiel de l'hôtel Oran Bay et des coordonnées.
    * **Voix-Off :** *« Que ce soit pour affaires ou pour un séjour d'exception… découvrez l'art de vivre cinq étoiles. Oran Bay Hotel vous accueille. »*
    * **Texte Écran :** 
      ```
      ORAN BAY HOTEL *****
      L'Excellence à Oran
      [www.oranbayhotel.com](https://www.oranbayhotel.com) | +213 (0) 41 98 00 00
      ```
    """)

st.markdown("---")

# Bloc complet au format texte pour copier/télécharger
st.header("📄 Fichier Texte Complet (Pour la Production)")

script_complet = """================================================================================
          SCRIPT VIDÉO PUBLICITAIRE — HOTEL 5 ÉTOILES ORAN BAY
================================================================================
Titre du projet : L'Élégance face à la Méditerranée
Format          : Télévision & Réseaux Sociaux (Reels / TikTok / YouTube)
Durée totale    : 45 secondes
Ambiance sonore : Musique lounge/électro élégante
================================================================================

[00:00 - 00:07] — INTRODUCTION & VUE PANORAMIQUE
• Visuel       : Plan au drone de la baie d'Oran au lever du soleil.
• Voix-Off     : « Au cœur de la majestueuse baie d'Oran, là où le ciel rencontre la Méditerranée… découvrez un écran de raffinement et d'élégance absolue. »
• Texte Écran  : Bienvenue à l'Oran Bay Hotel *****

[00:07 - 00:15] — SUITES & VUE SUR MER
• Visuel       : Ouverture des rideaux d'une suite exécutive avec vue mer.
• Voix-Off     : « Éveillez vos sens dans des suites d'exception, baignées de lumière, offrant une vue panoramique sur l'horizon marine. »
• Texte Écran  : Des Espaces Pensés Pour Votre Confort

[00:15 - 00:25] — GASTRONOMIE & RESTAURATION
• Visuel       : Dressage d'un plat par le chef et service de cocktail.
• Voix-Off     : « Laissez-vous séduire par une gastronomie raffinée, où chaque création de nos chefs est une véritable invitation au voyage. »
• Texte Écran  : Une Expérience Gastronomique Unique

[00:25 - 00:35] — PISCINE & BIEN-ÊTRE
• Visuel       : Piscine extérieure ensoleillée et ambiance spa.
• Voix-Off     : « Ressourcez-vous au bord de nos espaces aquatiques ou profitez d'un moment de sérénité au sein de notre spa d'exception. »
• Texte Écran  : Sérénité & Détente Absolue

[00:35 - 00:45] — CONCLUSION & APPEL À L'ACTION
• Visuel       : Vue nocturne illuminée de l'hôtel et apparition du logo.
• Voix-Off     : « Que ce soit pour affaires ou pour un séjour d'exception… découvrez l'art de vivre cinq étoiles. Oran Bay Hotel vous accueille. »
• Texte Écran  : ORAN BAY HOTEL ***** | www.oranbayhotel.com
================================================================================"""

st.code(script_complet, language="text")

st.download_button(
    label="💾 Télécharger le Script (.txt)",
    data=script_complet,
    file_name="Script_Publicite_Oran_Bay.txt",
    mime="text/plain",
)
