# Dictionnaire des Données - "Le Terroir Gourmand"

Ce fichier décrit la structure du dataset `transactions_terroir_gourmand.csv`. Ce jeu de données regroupe 12 mois de transactions financières simulées pour une PME de restauration.

### Structure des colonnes

| Nom de la colonne | Type | Description | Usage dans le projet |
| --- | --- | --- | --- |
| **`date`** | DateTime | Date précise de la transaction (AAAA-MM-JJ). | Index temporel indispensable pour le modèle **Prophet**.
| **`montant`** | Float | Valeur en FCFA. Positif (entrées/ventes) ou négatif (charges/achats). | Variable principale (`y`) pour la prévision de la trésorerie. |
| **`type`** | String | Catégorie de l'opération (ex: Vente, Achat_Stock, Salaire, Loyer). | Utilisé pour segmenter l'analyse financière par type de flux. |
| **`beneficiaire`** | String | Identité du fournisseur ou du client impliqué. | Utilisé pour détecter des bénéficiaires inhabituels (fraude). |
| **`heure_transaction`** | Integer | Heure de l'opération (format 0-23). | Critère clé pour identifier les activités suspectes nocturnes. |
| **`solde_cumule`** | Float | État du compte après chaque opération. | Indicateur visuel pour le Dashboard de santé financière. |
| **`est_fraude`** | Integer | Label binaire : **1** (suspect) ou **0** (sain). | Variable cible pour entraîner et valider **Isolation Forest**. |
