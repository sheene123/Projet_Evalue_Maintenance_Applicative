# Maintenances réalisées

Ce document classe les modifications apportées à l'application initiale selon les
**quatre dimensions de la maintenance applicative**, avec l'emplacement dans le code
et la Pull Request correspondante.

## Vue d'ensemble

| Type | Modification | Fichier(s) | PR |
|------|--------------|-----------|----|
| Perfective | Extraction de la logique métier dans `convert()` | `app_functions.py`, `app.py` | #1 |
| Corrective | Validation des montants ≤ 0 et des devises identiques + messages d'erreur | `app_functions.py`, `app.py` | #2 |
| Perfective | Tests unitaires de `convert()` | `test_app.py` | #3 |
| Évolutive | Bouton d'inversion des devises + ajout GBP/CAD | `app.py`, `app_functions.py` | #4 |
| Perfective | CI GitHub Actions (flake8, black, pytest) | `.github/workflows/`, `requirements.txt` | #5 |
| Évolutive | Historique des conversions (`session_state`) | `app.py` | #6 |
| Adaptative | Taux via API externe + repli | `app_functions.py`, `app.py` | #7 |

## Détail

### Maintenance corrective (PR #2)
L'application initiale ne gérait ni les montants invalides ni la conversion d'une devise
vers elle-même. `convert()` renvoie désormais `None` pour un montant nul ou négatif et
le montant inchangé pour deux devises identiques ; `app.py` affiche un message d'erreur
clair dans ces cas au lieu de calculer un résultat incohérent.

### Maintenance évolutive (PR #4 et #6)
Ajout de fonctionnalités demandées : un bouton pour **inverser** les devises, deux
**nouvelles devises** (GBP, CAD) et un **historique** des conversions conservé dans
`st.session_state` pendant la session.

### Maintenance adaptative (PR #7)
Les taux codés en dur sont remplacés par des taux récupérés via l'**API
exchangerate-api.com** (`get_rates()`). Pour s'adapter à l'indisponibilité éventuelle de
l'API (pas de clé, erreur réseau), un **repli** sur `FALLBACK_RATES` garantit que
l'application reste fonctionnelle.

### Maintenance perfective (PR #1, #3 et #5)
Amélioration de la qualité et de la structure : la **logique métier** est isolée dans
`app_functions.py` (testable sans Streamlit), des **tests unitaires** couvrent `convert()`,
et une **chaîne d'intégration continue** (flake8, black, pytest) garantit un code propre
et testé avant chaque merge.
