import streamlit as st

from app_functions import FALLBACK_RATES, convert

st.title("Convertisseur de devises")

# La logique de calcul vit désormais dans app_functions.convert()
# (refactoring : l'interface ne fait plus que de l'affichage).
rates = FALLBACK_RATES

amount = st.number_input("Montant :", min_value=0.0, format="%.2f")
from_currency = st.selectbox("De :", list(rates.keys()))
to_currency = st.selectbox("Vers :", list(rates.keys()))

if st.button("Convertir"):
    result = convert(amount, from_currency, to_currency, rates)
    st.success(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
