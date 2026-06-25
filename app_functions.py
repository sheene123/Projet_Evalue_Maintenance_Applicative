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

    Le calcul passe par la base commune des taux : on ramène le montant en
    devise de base puis on le reconvertit vers la devise cible.
    """
    return amount * rates[to_currency] / rates[from_currency]
