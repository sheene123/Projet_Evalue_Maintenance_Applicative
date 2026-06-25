import streamlit as st

from app_functions import convert, get_rates

# Devises proposées dans l'interface (l'API en renvoie beaucoup plus).
SUPPORTED = ["EUR", "USD", "JPY", "GBP", "CAD"]

st.title("Convertisseur de devises")

# Maintenance adaptative : taux récupérés via une API externe (avec repli).
api_key = st.text_input("Clé API exchangerate-api.com (optionnel)", type="password")
all_rates, source = get_rates(base="EUR", api_key=api_key)
st.caption(f"Source des taux : {source}")

rates = {c: all_rates[c] for c in SUPPORTED if c in all_rates}
currencies = list(rates.keys())

# Valeurs par défaut des devises (nécessaires pour le bouton d'inversion).
if "from_currency" not in st.session_state:
    st.session_state.from_currency = currencies[0]
if "to_currency" not in st.session_state:
    st.session_state.to_currency = currencies[1]
# Maintenance évolutive : historique des conversions de la session.
if "history" not in st.session_state:
    st.session_state.history = []


def swap_currencies():
    """Maintenance évolutive : inverse les deux devises sélectionnées."""
    st.session_state.from_currency, st.session_state.to_currency = (
        st.session_state.to_currency,
        st.session_state.from_currency,
    )


def clear_history():
    st.session_state.history = []


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
            line = f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}"
            st.success(line)
            st.session_state.history.append(line)

# Maintenance évolutive : affichage de l'historique des conversions.
if st.session_state.history:
    st.subheader("Historique des conversions")
    for entry in reversed(st.session_state.history):
        st.write(entry)
    st.button("Effacer l'historique", on_click=clear_history)
