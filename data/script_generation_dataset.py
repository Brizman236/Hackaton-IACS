import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# --- 1. CONFIGURATION ---
np.random.seed(42)
start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 12, 31)
dates = pd.date_range(start=start_date, end=end_date)

# --- 2. GÉNÉRATION DU CALENDRIER DES ÉVÉNEMENTS (CSV) ---
events_data = {
    'ds': ['2026-02-18', '2026-03-20', '2026-05-24'],
    'holiday': ['Debut_Ramadan', 'Korite', 'Tabaski'],
    'lower_window': [0, -1, -1],
    'upper_window': [30, 1, 1]
}
df_events = pd.DataFrame(events_data)
df_events.to_csv('calendrier_events_senegal.csv', index=False)

# --- 3. GÉNÉRATION DES TRANSACTIONS (CSV) ---
transactions = []

for date in dates:
    # Définition des contextes (Ramadan, Tabaski, Jours normaux)
    is_ramadan = (date >= datetime(2026, 2, 18)) & (date <= datetime(2026, 3, 19))
    is_tabaski = (date == datetime(2026, 5, 24))
    
    # Nombre de transactions quotidiennes (moyenne pour un restaurant)
    n_trans = 0 if is_tabaski else np.random.randint(40, 70)
    
    for _ in range(n_trans):
        # Type de transaction
        t_type = np.random.choice(['Vente', 'Achat_Marche', 'Salaire', 'Loyer'], 
                                  p=[0.8, 0.15, 0.02, 0.03])
        
        # Montant selon le type
        if t_type == 'Vente':
            # Effet Ramadan : moins de ventes le jour, pic le soir (ici on simule une baisse globale)
            base = 4000 if not is_ramadan else 2500
            amount = np.random.normal(base, 1000)
        elif t_type == 'Achat_Marche':
            amount = -np.random.normal(150000, 30000) # Gros achat marché le matin
        else:
            amount = -np.random.randint(200000, 500000)
            
        # Injection de Fraude (3% des transactions)
        is_fraud = 0
        if np.random.rand() < 0.03:
            is_fraud = 1
            # Fraude : Facture fournisseur gonflée
            amount = amount * 2 if amount < 0 else amount * 1.5
            
        transactions.append([date, amount, t_type, is_fraud])

# Création du DataFrame et sauvegarde
df_trans = pd.DataFrame(transactions, columns=['date', 'montant', 'type', 'est_fraude'])
df_trans.to_csv('transactions_terroir_gourmand.csv', index=False)

print("Génération terminée :")
print("- 'calendrier_events_senegal.csv' créé.")
print("- 'transactions_terroir_gourmand.csv' créé.")
