"""
Pipelines entraînés
Que sont les pipelines entraînés ?
    - Des modèles qui permettent à spaCy de prédire les attributs linguistiques en contexte
        - Étiquetage de partie du discours
        - Dépendances syntaxiques
        - Entités nommées
    - Entrainés sur des exemples de textes labellisés
    - Peuvent être améliorés avec des exemples supplémentaires

spaCy propose un certain nombre de paquets de pipelines entraînés que tu peux télécharger avec la commande spacy download.
Par exemple, le paquet "fr_core_news_sm" est un petit pipeline pour la langue française qui propose toutes les fonctionnalités de base et qui a été entraîné sur des textes d'actualité.

La méthode spacy.load charge un paquet de pipeline à partir de son nom et retourne un objet nlp.

Le paquet contient les poids binaires qui permettent à spaCy d'effectuer des prédictions.

Il inclut aussi le vocabulaire, des méta-informations à propos du pipeline et le fichier de configuration utilisé pour l'entraîner.
Cela indique à spaCy quelle classe de langue utiliser et comment configurer le pipeline de traitements.

Doc d'installation ici: https://spacy.io/usage/models
"""

import spacy
#Paquets de pipelines
# Un paquet avec le label fr_core_news_sm
#$ python -m spacy download fr_core_news_sm
# Version poetry
#$ poetry run spacy download fr_core_news_sm

#Poids binaires
#Vocabulaire
#Méta-information
#Fichier de configuration
#Prédiction des étiquettes de partie de discours

# Charge le petit pipeline français
nlp = spacy.load("fr_core_news_sm")

# Traite le texte
doc = nlp("Elle mangea la pizza")

# Itère sur les tokens
for token in doc:
    # Affiche le texte et l'étiquette de partie de discours prédite
    print(token.text, token.pos_)

# Prédiction de dépendances syntaxiques
# En plus des étiquettes de partie de discours, nous pouvons aussi prédire comment les mots sont reliés.
# Par exemple, si un mot est le sujet ou un objet d'une phrase.
for token in doc:
    # L'attribut .dep_ retourne la dépendance syntaxique prédite.
    # L'attribut .head retourne le token de tête syntaxique ou noyau.
    # Tu peux le voir comme le token parent auquel le mot considéré se rattache.
    print(token.text, token.pos_, token.dep_, token.head.text)

# Prédiction d'entités nommées
# Traite le texte
doc = nlp("Apple conçoit le nouvel iPhone à Cupertino.")

# Itère sur les entités prédites Les entités nommées sont des "objets du monde réel" auxquels on assigne un nom -
# par exemple, une personne, une organisation ou un pays.
for ent in doc.ents: # doc.ents --> entités nommées prédites par le modèle.
    # Elle retourne un itérateur d'objets Span,
    # donc nous pouvons imprimer le texte de l'entité et son label en utilisant l'attribut .label_.
    # Affiche le texte de l'entité et son label
    print(ent.text, ent.label_)

# Astuce : la méthode spacy.explain
# Obtiens des définitions rapides des tags et des étiquettes les plus courants.
# Cela s'applique aussi aux étiquettes de partie de discours et aux dépendances syntaxiques.
print(spacy.explain("GPE"))
print(spacy.explain("NNP"))
print(spacy.explain("dobj"))

text = "Apple a été créée en 1976 par Steve Wozniak, Steve Jobs et Ron Wayne."

# Traite le texte
doc = nlp(text)

# Affiche le texte du document
print(doc.text)

text = "Apple a été créée en 1976 par Steve Wozniak, Steve Jobs et Ron Wayne."

# Traite le texte
doc = nlp(text)

for token in doc:
    # Obtiens le texte du token, sa partie de discours et sa relation de dépendance
    token_text = token.text
    token_pos = token.pos_
    token_dep = token.dep_
    # Ceci sert uniquement au formatage de l'affichage
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")

# Itère sur les entités prédites
for ent in doc.ents:
    # Affiche le texte de l'entité et son label
    print(ent.text, ent.label_)