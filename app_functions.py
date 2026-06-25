"""Logique métier du convertisseur de devises.

Séparée de l'interface Streamlit (maintenance perfective) pour pouvoir
être testée unitairement sans lancer l'application.
"""

# Taux de secours (base EUR = 1) utilisés tant qu'aucune API n'est branchée.
FALLBACK_RATES = {
    "EUR": 1.0,
    "USD": 1.1,
    "JPY": 130.0,
}


def convert(amount, from_currency, to_currency, rates):
    """Convertit un montant d'une devise source vers une devise cible.

    Maintenance corrective :
    - renvoie ``None`` si le montant est nul ou négatif ;
    - renvoie le montant inchangé si les deux devises sont identiques.
    """
    if amount is None or amount <= 0:
        return None
    if from_currency == to_currency:
        return amount
    return amount * rates[to_currency] / rates[from_currency]
