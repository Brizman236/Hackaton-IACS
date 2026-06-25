import pandas as pd

# Définition des événements majeurs pour l'année 2026 au Sénégal
# Les fenêtres (windows) indiquent à Prophet d'étendre l'effet de la fête 
# quelques jours avant ou après la date précise.
events = {
    'ds': [
        '2026-02-18', # Début Ramadan
        '2026-03-20', # Korité
        '2026-04-04', # Fête de l'Indépendance
        '2026-05-25', # Tabaski
    ],
    'holiday': [
        'Ramadan_Debut',
        'Korite',
        'Fete_Independance',
        'Tabaski'
    ],
    'lower_window': [0, -2, 0, -2],
    'upper_window': [30, 2, 0, 2]
}

# Création du DataFrame
df_events = pd.DataFrame(events)

# Conversion de la colonne date au format datetime pour la sécurité
df_events['ds'] = pd.to_datetime(df_events['ds'])

# Sauvegarde
df_events.to_csv('calendrier_events_senegal.csv', index=False)

print("Fichier 'calendrier_events_senegal.csv' généré avec succès.")