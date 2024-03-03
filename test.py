import pandas as pd
import matplotlib.pyplot as plt
from optimized import maximiser_benefices_optimise

# Fonction pour lire les données à partir d'un fichier CSV
def lire_actions_csv(chemin_fichier):
    actions = []
    with open(chemin_fichier, 'r') as file:
        next(file)  # Ignorer l'en-tête
        for line in file:
            name, price, profit = line.strip().split(',')
            actions.append((name, float(price), float(profit)))
    return actions

# Fonction pour lire les données à partir d'un fichier TXT
def lire_actions_txt(chemin_fichier):
    actions = []
    with open(chemin_fichier, 'r') as file:
        for line in file:
            name, price, profit = line.strip().split('\t')
            actions.append((name, float(price), float(profit)))
    return actions


# Fonction pour exécuter l'algorithme et obtenir les décisions prédites
def obtenir_decisions_algorithme(donnees_financieres):
    actions = lire_actions_csv("dataset2_Python+P7.csv")  # Charger les données d'actions depuis un fichier CSV
    budget_max = 500  # Définir le budget maximum
    
    # Exécuter l'algorithme sur les données financières historiques
    decisions_algorithme, _ = maximiser_benefices_optimise(actions, budget_max)
    
    # Créer un DataFrame avec les décisions d'investissement prédites
    df_decisions_algorithme = pd.DataFrame(decisions_algorithme, columns=['Decision_Algorithme'])
    
    return df_decisions_algorithme

# Fonction pour lire les décisions d'investissement de Sienna
def lire_decisions_sienna(chemin_fichier):
    # Les décisions de Sienna sont fournies dans le texte directement, nous n'avons pas besoin de lire un fichier
    # Nous allons simplement extraire les valeurs de coût total et de profit total à partir du texte
    
    # Informations sur les décisions de Sienna
    decisions_sienna = []

    # Décision 1
    decision1 = {
        "Shares": ["GRUT"],
        "Total cost": 498.76,
        "Total return": 196.61
    }
    decisions_sienna.append(decision1)

    # Décision 2
    decision2 = {
        "Shares": ["ECAQ", "IXCI", "FWBE", "ZOFA", "PLLK", "YFVZ", "ANFX", "PATS", "NDKR", "ALIY", "JWGF", "JGTW", "FAPS", "VCAX", "LFXB", "DWSK", "XQII", "ROOM"],
        "Total cost": 489.24,
        "Profit": 193.78
    }
    decisions_sienna.append(decision2)

    return decisions_sienna

# Charger les données financières historiques depuis le premier fichier CSV
donnees_financieres_1 = pd.read_csv("dataset1_Python+P7.csv")

# Charger les décisions d'investissement de Sienna
decisions_sienna_1 = lire_decisions_sienna("solution1_Python+P7.txt")

# Charger les données financières historiques depuis le deuxième fichier CSV
donnees_financieres_2 = pd.read_csv("dataset2_Python+P7.csv")

# Charger les décisions d'investissement de Sienna
decisions_sienna_2 = lire_decisions_sienna("solution2_Python+P7.txt")

# Obtenir les décisions d'investissement prédites par l'algorithme
decisions_algorithme_1 = obtenir_decisions_algorithme(donnees_financieres_1)
decisions_algorithme_2 = obtenir_decisions_algorithme(donnees_financieres_2)

# Comparaison des résultats de l'algorithme avec les décisions de Sienna pour le premier jeu de données
plt.figure(figsize=(10, 6))
plt.plot(decisions_algorithme_1['Decision_Algorithme'], label='Décisions de l\'algorithme (Dataset 1)', color='red')
print(decisions_sienna_1)
plt.plot(range(len(decisions_sienna_1)), decisions_sienna_1['Total cost'], label='Coût total de Sienna (Dataset 1)', color='blue')
plt.plot(range(len(decisions_sienna_1)), decisions_sienna_1['Total return'], label='Retour total de Sienna (Dataset 1)', color='green')

# Comparaison des résultats de l'algorithme avec les décisions de Sienna pour le deuxième jeu de données
plt.plot(decisions_algorithme_2['Decision_Algorithme'], label='Décisions de l\'algorithme (Dataset 2)', color='orange')
plt.plot(range(len(decisions_sienna_2)), decisions_sienna_2['Total cost'], label='Coût total de Sienna (Dataset 2)', color='purple')
plt.plot(range(len(decisions_sienna_2)), decisions_sienna_2['Profit'], label='Profit de Sienna (Dataset 2)', color='brown')

# Afficher la légende et le titre du graphique
plt.title('Comparaison des Décisions d\'Investissement')
plt.xlabel('Décision')
plt.ylabel('Valeur')
plt.legend()
plt.show()
