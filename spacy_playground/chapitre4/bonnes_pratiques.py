"""
Problème 1 : Les modèles peuvent "oublier" des choses

    Les modèles existants peuvent sur-optimiser sur les nouvelles données
        ex. : si tu l'actualises uniquement avec "SITE_WEB", il peut "oublier" ce qu'est une personne avec le label "PER"
    On appelle ça le problème de "l'oubli catastrophique"

Solution 1 : Incorporer des prédictions précédemment correctes

    Par exemple, si tu l'entraînes sur "SITE_WEB", inclus aussi des exemples de "PER"

    Fais tourner un modèle existant de spaCy sur les données et extrais toutes les autres entités pertinentes

Problème 2 : Les modèles ne peuvent pas tout apprendre

    Les modèles de spaCy effectuent des prédictions basées sur le contexte local

    Les modèles peuvent avoir des difficultés à apprendre si la décision est difficile à prendre en se basant sur le contexte

    Les schémas de labellisation doivent être cohérents et pas trop spécifiques

    Par exemple: "VETEMENTS" est préférable à "VETEMENTS_ADULTES" et "VETEMENTS_ENFANTS"

Solution 2 : Planifie soigneusement ton schéma de labellisation

    Choisis des catégories qui sont représentées dans le contexte local

    Mieux vaut être trop générique que trop spécifique

    Utilise des règles pour passer de labels génériques à des catégories spécifiques

    MAUVAIS :
        LABELS = ["CHAUSSURES_ADULTES", "CHAUSSURES_ENFANTS", "MES_GROUPES_PREFERES"]

    BON :
        LABELS = ["VETEMENTS", "GROUPE_MUSICAL"]

"""
