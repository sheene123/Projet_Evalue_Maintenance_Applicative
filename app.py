import streamlit as st

from app_functions import FALLBACK_RATES, convert

st.title("Convertisseur de devises")

rates = FALLBACK_RATES

amount = st.number_input("Montant :", min_value=0.0, format="%.2f")
from_currency = st.selectbox("De :", list(rates.keys()))
to_currency = st.selectbox("Vers :", list(rates.keys()))

if st.button("Convertir"):
    # Maintenance corrective : on bloque les cas invalides avec un message clair.
    if from_currency == to_currency:
        st.error("La devise source et la devise cible doivent être différentes.")
    else:
        result = convert(amount, from_currency, to_currency, rates)
        if result is None:
            st.error("Le montant doit être strictement positif.")
        else:
            st.success(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
