from itertools import combinations

# Lire les données à partir du fichier et les stocker
def lire_actions(fichier):
    actions = []
    with open(fichier, 'r') as file:
        for ligne in file:
            action, cout, benefice = ligne.strip().split('\t')
            actions.append((action, int(cout), float(benefice)))
    return actions

# Trouver la meilleure combinaison d'actions
def maximiser_benefices(actions, budget_max):
    meilleure_combinaison = None
    meilleur_profit = 0

    # Générer toutes les combinaisons possibles d'actions
    for taille_combinaison in range(1, len(actions) + 1):
        combinaisons = combinations(actions, taille_combinaison)

        # Parcourir chaque combinaison
        for combinaison in combinaisons:
<<<<<<< HEAD
            pass
=======
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
>>>>>>> d56c1be35d548976689a1c7047b6a17061231911
