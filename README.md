# Mini-Convertisseur de devises

Application **Streamlit** de conversion de devises, réalisée dans le cadre du projet
de **maintenance applicative** (séance 5). Le but du projet est d'appliquer les quatre
dimensions de la maintenance (corrective, évolutive, adaptative, perfective) à une
application simple volontairement imparfaite.

## Fonctionnalités

- Conversion entre **5 devises** : EUR, USD, JPY, GBP, CAD.
- **Validation** : refus des montants nuls ou négatifs et des devises identiques, avec
  message d'erreur clair.
- **Inversion** des devises source/cible en un clic.
- **Historique** des conversions de la session (avec bouton pour l'effacer).
- **Taux en temps réel** via l'API exchangerate-api.com, avec **repli automatique** sur
  des taux de secours si aucune clé n'est fournie ou en cas d'erreur réseau.

## Structure du projet

| Fichier | Rôle |
|---------|------|
| `app.py` | Interface Streamlit |
| `app_functions.py` | Logique métier : `convert()`, `get_rates()`, `FALLBACK_RATES` |
| `test_app.py` | Tests unitaires (pytest) |
| `.github/workflows/python-tests.yml` | CI : flake8 + black + pytest |
| `requirements.txt` | Dépendances |
| `REPARTITION_TACHES.md` | Répartition des tâches du groupe |
| `MAINTENANCE.md` | Détail des maintenances réalisées |
| `REPONSES_QUESTIONS.md` | Réponses aux questions de réflexion |

## Installation

```bash
python -m venv .venv
source .venv/bin/activate      # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

## Lancement

```bash
streamlit run app.py
```

### Clé API (optionnelle)

Sans clé, l'application utilise des **taux de secours** codés dans `FALLBACK_RATES`.
Pour des taux en direct, créez une clé gratuite sur
[exchangerate-api.com](https://www.exchangerate-api.com/) et saisissez-la dans le champ
prévu dans l'interface.

## Tests et qualité

```bash
pytest                  # tests unitaires
flake8 . --max-line-length=100
black --check .
```

Ces trois contrôles sont exécutés automatiquement par **GitHub Actions** à chaque push
et à chaque Pull Request vers `main`.

## Organisation du travail (groupe de 2)

Le travail a été réparti à l'aide d'un **GitHub Project** (tableau Kanban) et d'**issues**
numérotées : [Project « @repartision tache »](https://github.com/users/sheene123/projects/5).

- Chaque tâche correspond à une **issue** assignée à un membre du groupe
  (voir [`REPARTITION_TACHES.md`](REPARTITION_TACHES.md)).
- Chaque tâche est développée sur sa **propre branche** (`feature/…`, `bugfix/…`,
  `docs/…`) puis intégrée via une **Pull Request** documentée — jamais de push direct
  sur `main`.
- La CI doit être verte avant chaque merge.

Membres : **noe-cervera** et **sheene123**.
