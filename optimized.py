from bruteforce import lire_actions

def maximiser_benefices_optimise(actions, budget_max):
    # Nombre total d'actions
    n = len(actions)
    
    # Matrice pour stocker les valeurs intermédiaires
    # dp[i][j] : le bénéfice maximal avec les i premières actions et un budget de j
    dp = [[0] * (budget_max + 1) for _ in range(n + 1)]

    # Remplir la matrice par programmation dynamique
    for i in range(1, n + 1):  
        for j in range(1, budget_max + 1):  
            # condition pour vérifier que le coût de l'action est inférieur ou égal au budget
            if actions[i - 1][1] <= j:
                dp[i][j] = max(dp[i - 1][j], actions[i - 1][2] + dp[i - 1][j - actions[i - 1][1]])
            else:
                dp[i][j] = dp[i - 1][j]

    # Retrouver la meilleure combinaison d'actions
    meilleur_profit = dp[n][budget_max]  
    budget_restant = budget_max
    meilleure_combinaison = []
    for i in range(n, 0, -1):  
        # Si le bénéfice a été obtenu en incluant l'action actuelle
        if dp[i][budget_restant] != dp[i - 1][budget_restant]:
            meilleure_combinaison.append(actions[i - 1])
            budget_restant -= actions[i - 1][1]

    return meilleure_combinaison[::-1], meilleur_profit

if __name__ == "__main__":
    chemin_fichier = 'actions.txt'  
    budget_limite = 500 

    donnees_actions = lire_actions(chemin_fichier)
    meilleure_combinaison, meilleur_profit = maximiser_benefices_optimise(donnees_actions, budget_limite)

    print("Meilleure Combinaison:", meilleure_combinaison)
    print("Meilleur Profit:", meilleur_profit)




