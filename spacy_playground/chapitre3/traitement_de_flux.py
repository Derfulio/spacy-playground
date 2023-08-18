"""
Traitement de flux

Dans cet exercice, tu vas utiliser nlp.pipe pour un traitement plus efficace du texte.
L’objet nlp a déjà été créé pour toi.
Une liste de tweets à propos d’une chaîne américaine connue de fast-food est disponible via la variable nommée TEXTS.

Partie 1
    Réécris l’exemple pour utiliser nlp.pipe.
    Au lieu d’itérer sur les textes et de les traiter,
    itère sur les objets doc générés par nlp.pipe.

Partie 2
    Réécris l’exemple pour utiliser nlp.pipe.
    N’oublie pas d’appeler list() sur le résultat pour le transformer en liste.

Partie 3
    Réécris l’exemple pour utiliser nlp.pipe.
    N’oublie pas d’appeler list() sur le résultat pour le transformer en liste.
"""
import json
import spacy

TEXTS = [
    "McDonalds est le meilleur restaurant que je connaisse.",
    "Ces illuminés sont vent debout contre Linky mais pensent qu'on leur sert de la véritable viande chez McDonalds dans un burger à 1 €",
    "Les gens continuent vraiment de manger au McDo :(",
    "On trouve des chicken wings au McDo en Espagne. Je revis ",
    "@McDonalds s'il vous plait rendez-nous le meilleur burger au monde !!....Le Mc Camembert :P",
    "hé ho le #MacDo dépêchez-vous d'ouvrir. J'AI UNE FAIM DE LOUP :D",
    "Ce matin j'ai cédé en allant au Macdo et maintenant mon estomac me le fait payer",
]

nlp = spacy.load("fr_core_news_sm")

# with open("exercises/fr/tweets.json", encoding="utf8") as f:
#   TEXTS = json.loads(f.read())

# Partie 1
# Traite les textes et affiche les adjectifs
# for text in TEXTS:
#   doc = nlp(text)
#  print([token.text for token in doc if token.pos_ == "ADJ"])
for doc in nlp.pipe(TEXTS):
    print([token.text for token in doc if token.pos_ == "ADJ"])

# Partie 2
# Traite les textes et affiche les entités
# docs = [nlp(text) for text in TEXTS]
docs = list(nlp.pipe(TEXTS))
entities = [doc.ents for doc in docs]
print(*entities)

# Partie 3
nlp = spacy.blank("fr")

people = ["David Bowie", "Angela Merkel", "Lady Gaga"]

# Crée une liste de motifs pour le PhraseMatcher
# patterns = [nlp(person) for person in people]
patterns = list(nlp.pipe(people))
