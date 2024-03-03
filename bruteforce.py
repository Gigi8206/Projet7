from itertools import combinations

# Lire les données à partir du fichier et les stocker
def lire_actions(chemin_fichier):
    actions = []
    with open(chemin_fichier, 'r') as file:
        lines = file.readlines()
    for line in lines:
        # Diviser chaque ligne en utilisant des espaces comme séparateur
        action, cout, benefice = line.strip().split()
        actions.append((action, int(cout), float(benefice)))
    return actions


# Trouver la meilleure combinaison d'actions
def maximiser_benefices(actions, budget_max):
    meilleure_combinaison = None
    meilleur_profit = 0

    for taille_combinaison in range(1, len(actions) + 1):
        combinaisons = combinations(actions, taille_combinaison)

        # Parcourir chaque combinaison
        for combinaison in combinaisons:
            total_cout = sum(cout for _, cout, _ in combinaison)
            total_benefice = sum(benefice for _, _, benefice in combinaison)
            
            # Vérifier si la combinaison est dans la limite du budget et a un profit plus élevé
            if total_cout <= budget_max and total_benefice > meilleur_profit:
                meilleure_combinaison = combinaison
                meilleur_profit = total_benefice

    return meilleure_combinaison, meilleur_profit

if __name__ == "__main__":
    chemin_fichier = 'actions.txt'  
    budget_limite = 500 

    donnees_actions = lire_actions(chemin_fichier)
    meilleure_combinaison, meilleur_profit = maximiser_benefices(donnees_actions, budget_limite)

    print("Meilleure Combinaison:", meilleure_combinaison)
    print("Meilleur Profit:", meilleur_profit)
