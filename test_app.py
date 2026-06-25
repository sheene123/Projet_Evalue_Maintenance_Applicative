"""Tests unitaires de la logique métier (maintenance perfective).

Lancement : ``pytest`` à la racine du projet.
"""

import pytest

from app_functions import FALLBACK_RATES, convert


def test_convert_eur_usd():
    rates = {"EUR": 1, "USD": 1.1}
    assert round(convert(10, "EUR", "USD", rates), 2) == 11.0


def test_convert_usd_eur():
    rates = {"EUR": 1, "USD": 1.1}
    assert round(convert(11, "USD", "EUR", rates), 2) == 10.0


def test_convert_same_currency_returns_amount():
    assert convert(10, "EUR", "EUR", FALLBACK_RATES) == 10


def test_convert_zero_amount_returns_none():
    assert convert(0, "EUR", "USD", FALLBACK_RATES) is None


def test_convert_negative_amount_returns_none():
    assert convert(-5, "EUR", "USD", FALLBACK_RATES) is None


def test_convert_unknown_currency_raises():
    with pytest.raises(KeyError):
        convert(10, "EUR", "XXX", {"EUR": 1})


def test_cas_qui_echoue_demo():
    # Cas volontairement FAUX pour démontrer l'échec du pipeline CI.
    # 10 EUR -> USD vaut 11.0, on affirme volontairement une valeur erronée.
    rates = {"EUR": 1, "USD": 1.1}
    assert convert(10, "EUR", "USD", rates) == 999
