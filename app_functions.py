"""Logique métier du convertisseur de devises.

Séparée de l'interface Streamlit (maintenance perfective) pour pouvoir
être testée unitairement sans lancer l'application.
"""

import requests

# Taux de secours (base EUR = 1) utilisés si l'API externe est indisponible.
FALLBACK_RATES = {
    "EUR": 1.0,
    "USD": 1.1,
    "JPY": 130.0,
    "GBP": 0.85,
    "CAD": 1.45,
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


def get_rates(base="EUR", api_key="", timeout=5):
    """Maintenance adaptative : récupère les taux via exchangerate-api.com.

    Retourne un tuple ``(rates, source)``. En l'absence de clé ou en cas
    d'erreur réseau / réponse invalide, on retombe sur ``FALLBACK_RATES``
    pour que l'application reste fonctionnelle.
    """
    if not api_key:
        return dict(FALLBACK_RATES), "taux de secours (aucune clé API)"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base}"
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        data = response.json()
        if data.get("result") != "success":
            return dict(FALLBACK_RATES), "taux de secours (réponse API invalide)"
        return data["conversion_rates"], "API en direct"
    except requests.RequestException:
        return dict(FALLBACK_RATES), "taux de secours (erreur réseau)"
