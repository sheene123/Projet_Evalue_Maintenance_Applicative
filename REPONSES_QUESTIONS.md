# Réponses aux questions de réflexion

## 1. Gestion de version

**Comment organiser le travail en groupe avec des branches ?**

Chaque tâche fait l'objet d'une **branche dédiée**, nommée selon son objet :
`feature/api-taux`, `bugfix/validation`, `feature/historique`, `docs/questions`, etc.
Chacun travaille ainsi **isolément** sur sa branche, sans perturber le travail des
autres ni la branche stable `main`. Les tâches indépendantes (qui touchent des fichiers
différents) avancent **en parallèle** ; seules celles qui modifient le même fichier sont
faites en séquence pour éviter les conflits. La répartition est pilotée par un
**GitHub Project** et des **issues** numérotées assignées à chaque membre.

**Quels avantages des Pull Requests par rapport à un push direct sur `main` ?**

- **Revue de code** : le binôme relit les changements avant l'intégration.
- **Intégration continue** : les tests et le lint s'exécutent automatiquement sur la PR ;
  on n'intègre que si tout est vert.
- **`main` reste toujours fonctionnelle** : le code instable vit sur la branche, pas sur
  `main`.
- **Traçabilité** : chaque PR documente *pourquoi* un changement a été fait et relie la
  modification à son issue (`Closes #N`).

## 2. Qualité et tests

**Qu'est-ce qu'un test unitaire et pourquoi est-il important ?**

Un test unitaire vérifie le comportement d'une **petite unité de code** isolée (ici la
fonction `convert()`) sur des cas précis : conversion normale, devises identiques,
montant nul/négatif, devise inconnue. Il est important car il **détecte les régressions**
automatiquement : si une modification casse un comportement attendu, le test échoue
immédiatement, sans test manuel fastidieux. Il sert aussi de **documentation vivante** du
comportement attendu.

**Pourquoi automatiser les tests dans GitHub Actions avant d'accepter une PR ?**

Pour **garantir que `main` reste toujours saine**. La CI rejoue les tests et les contrôles
de style sur un environnement neutre, indépendamment du poste de chaque développeur
(« ça marche chez moi » ne suffit pas). Les problèmes sont ainsi détectés **au plus tôt**,
avant le merge, ce qui évite d'introduire des bugs dans la base de code partagée.

## 3. Refactoring

**Quelles dettes techniques dans le code initial ?**

- Les **taux étaient codés en dur**.
- La **logique de conversion était mélangée à l'interface** Streamlit, donc non testable.
- **Aucune gestion d'erreur** (montant nul, même devise).
- **Aucun historique** des conversions.

**Quelles modifications ont amélioré la maintenabilité et la lisibilité ?**

- La logique métier a été **isolée dans `app_functions.py`** (`convert()`, `get_rates()`),
  ce qui la rend **testable** sans lancer l'interface.
- Des **fonctions dédiées** (inversion, effacement de l'historique) clarifient `app.py`.
- L'ajout de **tests** et d'une **CI** sécurise les évolutions futures.

## 4. Maintenance

**Classement des modifications selon les 4 types :**

| Type | Modifications |
|------|---------------|
| Corrective | Validation des montants ≤ 0, blocage des devises identiques, messages d'erreur |
| Évolutive | Bouton d'inversion, ajout des devises GBP/CAD, historique des conversions |
| Adaptative | Récupération des taux via une API externe + repli |
| Perfective | Refactoring dans `app_functions.py`, tests unitaires, intégration continue |

**Quelle partie semble la plus fréquente dans un projet réel ?**

Dans la vie d'un logiciel, ce sont surtout les maintenances **évolutive** et
**corrective** qui reviennent le plus souvent : les utilisateurs demandent en permanence
de nouvelles fonctionnalités et signalent des bugs à corriger. La maintenance
**adaptative** survient plus ponctuellement (changement d'API, de version, de plateforme),
et la maintenance **perfective** est un travail de fond continu mais moins visible.
