# Répartition des tâches — Projet Maintenance Applicative (Séance 5)

Projet de groupe (2 personnes) : **noe-cervera** & **sheene123**.
Application : Mini-Convertisseur de devises (Streamlit).

## Stratégie de branches

- Branche stable : `main` (on n'y pousse pas directement).
- Une branche par tâche, fusionnée via **Pull Request** documentée.
- Convention de nommage : `feature/...`, `bugfix/...`, `docs/...`.

## Ordre de réalisation et dépendances

```
#1 SOCLE (convert + FALLBACK_RATES)   <-- EN PREMIER, bloque tout
        |
   +----+-------------+
   v                  v
#2 Corrective      #3 Tests           (parallele)
   v                  v
#4 Inverser+devises #5 CI/qualite      (parallele : #5 fichier isole, 0 conflit)
   v
#6 Historique
   v
#7 API externe       (derniere modif d'app.py, la plus risquee)
        |
   +----+---------+
   v              v
#8 README app   #9 Reponses          (docs, parallele)
```

Les modifications d'`app.py` (#2 -> #4 -> #6 -> #7) sont **séquentielles** pour éviter
les conflits de merge ; pendant ce temps l'autre personne travaille sur des **fichiers
isolés** (`app_functions.py`, `test_app.py`, `.github/`, docs).

## Affectation

| #  | Tâche                                   | Type        | Branche                   | Dépend de | Assigné     |
|----|-----------------------------------------|-------------|---------------------------|-----------|-------------|
| 1  | Socle logique métier `convert()`        | Perfective  | feature/socle-metier      | —         | sheene123   |
| 2  | Validation montant + devises identiques | Corrective  | bugfix/validation         | #1        | noe-cervera |
| 3  | Tests unitaires `convert()`             | Perfective  | feature/tests             | #1        | sheene123   |
| 4  | Bouton inverser + devises GBP/CAD       | Évolutive   | feature/devises-inversion | #2        | noe-cervera |
| 5  | CI GitHub Actions + flake8/black        | Perfective  | feature/ci                | #3        | sheene123   |
| 6  | Historique (`session_state`)            | Évolutive   | feature/historique        | #4        | noe-cervera |
| 7  | Taux via API externe + repli            | Adaptative  | feature/api-taux          | #1, #6    | sheene123   |
| 8  | README.md + MAINTENANCE.md              | Docs        | docs/app-maintenance      | #2,#4,#6  | noe-cervera |
| 9  | REPONSES_QUESTIONS.md                   | Docs        | docs/questions            | tout      | sheene123   |

- **noe-cervera** : #2, #4, #6, #8 (interface `app.py` + doc app/maintenances)
- **sheene123** : #1, #3, #5, #7, #9 (logique, tests, CI, API, réponses)

## Ce qui peut être fait en parallèle

- #2 et #3 (dès que #1 est mergé).
- #4 et #5 (#5 ne touche aucun fichier partagé).
- #8 et #9 (documentation finale).
