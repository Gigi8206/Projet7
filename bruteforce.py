from itertools import combinations
#lire les données à partir du fichier et les stocker
def lire_actions(fichier):
    actions = []
    with open(fichier, 'r') as file:
        for ligne in file:
            action, cout, benefice = ligne.strip().split('\t')
            actions.append((action, int(cout), float(benefice)))
    return actions

# trouver la meilleure combinaison d'actions
def maximiser_benefices(actions, budget_max):
    meilleure_combinaison = None
    meilleur_profit = 0

# Générer toutes les combinaisons possibles d'actions
    for taille_combinaison in range(1, len(actions) + 1):
        combinaisons = combinations(actions, taille_combinaison)
          # Parcourir chaque combinaison
        for combinaison in combinaisons:
