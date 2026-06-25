import pandas as pd
import numpy as np
from datetime import datetime, timedelta, time

# Configuration
np.random.seed(42)
start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 12, 31)
dates = pd.date_range(start=start_date, end=end_date)

# Dictionnaire pour les bénéficiaires selon le type
beneficiaires_map = {
    'Vente': ['Client Direct', 'App Livraison', 'Entreprise B2B'],
    'Achat_Stock': ['Marché Sandaga', 'Fournisseur Poisson', 'Grossiste Boissons'],
    'Salaire': ['Personnel Cuisine', 'Serveurs', 'Manager'],
    'Loyer': ['Propriétaire Plateau'],
    'Impôt': ['Trésor Public'],
    'Virement_client': ['Entreprise B2B']
}

transactions = []

for date in dates:
    # Paramètres de saisonnalité
    is_ramadan = (date >= datetime(2026, 2, 18)) & (date <= datetime(2026, 3, 19))
    is_tabaski = (date == datetime(2026, 5, 24))
    
    n_trans = 0 if is_tabaski else np.random.randint(20, 50)
    
    for _ in range(n_trans):
        # Choix du type
        t_type = np.random.choice(['Vente', 'Achat_Stock', 'Salaire', 'Loyer', 'Impôt', 'Virement_client'], 
                                  p=[0.7, 0.2, 0.03, 0.02, 0.02, 0.03])
        
        # Montant
        base = 5000 if t_type == 'Vente' else 100000
        amount = np.random.normal(base, 1000) if t_type == 'Vente' else -np.random.normal(base, 20000)
        if t_type in ['Salaire', 'Loyer', 'Impôt']: amount = -np.random.randint(100000, 500000)
        
        # Heure de transaction (heures d'ouverture du restaurant)
        # Fraude possible entre 23h et 05h
        hour = np.random.choice(range(8, 23)) if np.random.rand() > 0.05 else np.random.choice(range(0, 6))
        
        # Injection de fraude
        is_fraud = 1 if (np.random.rand() < 0.03) or (hour < 6) else 0
        if is_fraud:
            amount = amount * 3 if amount > 0 else amount * 2
            
        beneficiaire = np.random.choice(beneficiaires_map[t_type])
        
        transactions.append({
            'date': date,
            'montant': amount,
            'type': t_type,
            'beneficiaire': beneficiaire,
            'heure_transaction': hour,
            'est_fraude': is_fraud
        })

# Création du DataFrame
df = pd.DataFrame(transactions)

# Calcul du solde cumulé
df = df.sort_values('date')
df['solde_cumule'] = df['montant'].cumsum()

# Sauvegarde
df.to_csv('transactions_terroir_gourmand.csv', index=False)
print("Dataset généré avec succès avec toutes les colonnes requises.")