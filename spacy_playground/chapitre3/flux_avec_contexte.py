"""
Traitement de données avec contexte

Dans cet exercice, tu vas utiliser des attributs personnalisés
pour ajouter aux citations des métadonnées sur l’auteur et le livre correspondants.

Une liste d’exemples sous la forme [text, context] est disponible via la variable DATA.
Les textes sont des citations de livres célèbres,
et les contextes sont des dictionnaires avec pour clés "author" et "book".

    _ Utilise la méthode set_extension pour déclarer les attributs personnalisés "author" et "book" sur le Doc,
    avec None comme valeur par défaut.
    _ Traite les paires [text, context] contenues dans DATA en utilisant nlp.pipe avec as_tuples=True.
    _ Actualise doc._.book et doc._.author avec les valeurs respectives d’informations obtenues avec le contexte.

"""

DATA = [
    [
        "Si ceux qui disent du mal de moi savaient exactement ce que je pense d'eux, ils en diraient bien davantage !",
        {"author": "Sacha Guitry", "book": "L'esprit"},
    ],
    [
        "Tu es responsable pour toujours de ce que tu as apprivoisé.",
        {"author": "Antoine de Saint-Exupéry", "book": "Le Petit Prince"},
    ],
    [
        "C'est justement la possibilité de réaliser un rêve qui rend la vie intéressante.",
        {"author": "Paulo Coelho", "book": "L'alchimiste"},
    ],
    [
        "Les seuls gens qui existent sont ceux qui ont la démence de vivre, de discourir, d'être sauvés, qui veulent jouir de tout dans un seul instant, ceux qui ne savent pas bâiller.",
        {"author": "Jack Kerouac", "book": "Sur la route"},
    ],
    [
        "C’est un jour d’avril froid et lumineux et les pendules sonnent 13 heures.",
        {"author": "George Orwell", "book": "1984"},
    ],
    [
        "Aujourd'hui, chacun sait le prix de toutes choses, et nul ne connaît la valeur de quoi que ce soit.",
        {"author": "Oscar Wilde", "book": "Le portrait de Dorian Gray"},
    ],
]

import json
import spacy
from spacy.tokens import Doc

# with open("exercises/fr/bookquotes.json", encoding="utf8") as f:
#   DATA = json.loads(f.read())

nlp = spacy.blank("fr")

# Déclare l'extension de Doc "author" (défaut None)
Doc.set_extension("author", default=None)

# Déclare l'extension de Doc "book" (default None)
Doc.set_extension("book", default=None)

for doc, context in nlp.pipe(DATA, as_tuples=True):
    # Définis les attributs doc._.book et doc._.author à partir du contexte
    doc._.book = context["book"]
    doc._.author = context["author"]

    # Affiche le texte et les données des attributs personnalisés
    print(f"{doc.text}\n — '{doc._.book}' par {doc._.author}\n")

# Cette même technique est utile pour de nombreuses taches.
# Par exemple, tu pourrais passer des numéros de page ou de paragraphe pour lier
# le Doc traité à sa position dans un plus grand document. Ou tu pourrais passer
# d'autres données structurées comme des ID faisant référence à une base de
# connaissances.
