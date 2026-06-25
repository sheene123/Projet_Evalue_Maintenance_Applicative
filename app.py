import streamlit as st

from app_functions import FALLBACK_RATES, convert

st.title("Convertisseur de devises")

rates = FALLBACK_RATES
currencies = list(rates.keys())

# Valeurs par défaut des devises (nécessaires pour le bouton d'inversion).
if "from_currency" not in st.session_state:
    st.session_state.from_currency = currencies[0]
if "to_currency" not in st.session_state:
    st.session_state.to_currency = currencies[1]


def swap_currencies():
    """Maintenance évolutive : inverse les deux devises sélectionnées."""
    st.session_state.from_currency, st.session_state.to_currency = (
        st.session_state.to_currency,
        st.session_state.from_currency,
    )


amount = st.number_input("Montant :", min_value=0.0, format="%.2f")

col1, col2 = st.columns(2)
with col1:
    from_currency = st.selectbox("De :", currencies, key="from_currency")
with col2:
    to_currency = st.selectbox("Vers :", currencies, key="to_currency")

st.button("Inverser les devises", on_click=swap_currencies)

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
