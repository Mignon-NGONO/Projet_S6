"""
Projet S6 : Analyseur de Budget Personnel et Taux d'Épargne
Nom : 
Date : 
"""

# ==============================================================================
# SECTION 1 : PROGRAMME PRINCIPAL (STRUCTURE GLOBALE)
# ==============================================================================

def main():
    print("=== PROJET S6 : ANALYSEUR DE BUDGET PERSONNEL ===")
    
    # TODO : 1. Demander le revenu mensuel total de l'utilisateur
    # Utiliser 'demander_nombre_positif()'
    revenu = demander_nombre_positif("Entrez votre revenu mensuel total (en FCFA) : ")
    
    # TODO : 2. Demander la liste des catégories de dépenses (ex: Loyer, Nourriture, Transport, Loisirs)
    # Astuce : Découper la saisie avec .split(",") ou faire une boucle
    categories = input("Entrez les catégories de dépenses séparées par des virgules (ex: Loyer, Nourriture, Transport) : ").split(",")
    
    
    # TODO : 3. Pour chaque catégorie, demander le montant dépense dans le mois
    # Stocker les données dans un dictionnaire 'depenses = {categorie: montant}'
    depenses = {}
    for categorie in categories:
        montant = demander_nombre_positif(f"Entrez le montant dépensé dans la catégorie '{categorie.strip()}' (en FCFA) : ")
        depenses[categorie.strip()] = montant

    # TODO : 4. Appeler 'calculer_total_depenses()' pour obtenir la somme des dépenses
    total_depenses = calculer_total_depenses(depenses)

    # TODO : 5. Appeler 'analyser_epargne()' pour calculer le solde et le taux d'épargne (%)
    epargne, taux_epargne = analyser_epargne(revenu, total_depenses)

    # TODO : 6. Appeler 'afficher_conseil_financier()' pour donner un bilan à l'utilisateur
    afficher_conseil_financier(revenu, total_depenses, epargne, taux_epargne)

    pass


# ==============================================================================
# SECTION 2 : FONCTION DE GESTION DES ERREURS
# ==============================================================================

def demander_nombre_positif(message):
    """
    TODO : Fonction pour sécuriser la saisie des montants.
    
    Consignes :
    1. Utiliser une boucle 'while True'.
    2. Utiliser un bloc 'try / except ValueError' contre les erreurs de texte.
    3. Vérifier que la valeur saisie est >= 0.
    4. Retourner la valeur sous forme de float.
    """
    while True:
        try:
            valeur = float(input(message))
            if valeur < 0:
                print("Erreur : La valeur doit être un nombre positif.")
                continue
            return valeur
        except ValueError:
            print("Erreur : Vous devez entrer un nombre valide.")

    pass


# ==============================================================================
# SECTION 3 : FONCTIONS DE CALCUL ET D'ANALYSE
# ==============================================================================

def calculer_total_depenses(dictionnaire_depenses):
    """
    TODO : Sommer toutes les dépenses du mois.
    
    Consignes :
    1. Initialiser une variable 'total' à 0.0.
    2. Parcourir les valeurs du dictionnaire avec une boucle 'for'.
    3. Ajouter chaque montant au total et retourner le résultat.
    """
    total=0.0
    for montant in dictionnaire_depenses.values():
        total += montant
    return total


def analyser_epargne(revenu, total_depenses):
    """
    TODO : Calculer le montant épargné et le taux d'épargne en %.
    
    Formules :
    - Epargne = Revenu - Total des dépenses
    - Taux d'épargne (%) = (Epargne / Revenu) * 100
    
    Consignes :
    1. Retourner les deux valeurs (l'épargne et le taux).
    """
    epargne = revenu - total_depenses
    taux_epargne = (epargne / revenu * 100) if revenu != 0 else 0
    return epargne, taux_epargne


# ==============================================================================
# SECTION 4 : AFFICHAGE DU BILAN FINANCIER
# ==============================================================================

def afficher_conseil_financier(revenu, total_depenses, epargne, taux_epargne):
    """
    TODO : Afficher un bilan clair avec des conseils adaptés.
    
    Consignes :
    1. Afficher le revenu, le total des dépenses, l'épargne restante et le taux (%).
    2. Utiliser des structures 'if / elif / else' :
       - Si taux_epargne >= 20 % -> Afficher que la gestion financière est excellente.
       - Si 0 <= taux_epargne < 20 % -> Afficher un conseil pour réduire certaines dépenses.
       - Si epargne < 0 (dépenses > revenu) -> Afficher une alerte de DÉFICIT / Surendettement !
    """
    print("\n=== BILAN FINANCIER ===")
    print(f"Revenu mensuel : {revenu:.2f} FCFA")
    print(f"Total des dépenses : {total_depenses:.2f} FCFA")
    print(f"Épargne restante : {epargne:.2f} FCFA")
    print(f"Taux d'épargne : {taux_epargne:.2f}%")

    if taux_epargne >= 20:
        print("Conseil : Votre gestion financière est excellente !")
    elif 0 <= taux_epargne < 20:
        print("Conseil : Essayez de réduire certaines dépenses pour améliorer votre épargne.")
    else:
        print("Alerte : Vous êtes en déficit ! Veuillez revoir votre budget.")

# ==============================================================================
# POINT D'ENTRÉE DU PROGRAMME
# ==============================================================================
if __name__ == "__main__":
    main()