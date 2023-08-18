"""
Scalabilité et performance

1 _ Traitement d'importantes quantités de texte
    Utilise la méthode nlp.pipe

    Traite des textes en tant que flux, génère des objets Doc

    Beaucoup plus rapide que d'appeler nlp sur chaque texte

    MAUVAIS :
        docs = [nlp(text) for text in LOTS_OF_TEXTS]
    BON :
        docs = list(nlp.pipe(LOTS_OF_TEXTS))

2 _ Intégration de contexte (1)
    Définir as_tuples=True dans nlp.pipe te permet de lui passer des tuples (text, context)

    Génère des tuples (doc, context)

    Utile pour ajouter des métadonnées au doc

    data = [
        ("Ceci est un texte", {"id": 1, "numero_page": 15}),
        ("Et un autre texte", {"id": 2, "numero_page": 16}),
    ]

    for doc, context in nlp.pipe(data, as_tuples=True):
        print(doc.text, context["numero_page"])

3 _ Utilisation isolée du Tokenizer
    Un autre scénario courant : Parfois tu as déjà un modèle chargé pour effectuer d'autres traitements,
    mais tu as seulement besoin du tokenizer pour un texte particulier.

    Lancer tout le pipeline est inutilement lent,
    parce que le modèle va te fournir tout un tas de prédictions dont tu n'as pas besoin.

    Utilise nlp.make_doc pour transformer un texte en un objet Doc

    MAUVAIS :
        doc = nlp("Bonjour monde !")
    BON :
        doc = nlp.make_doc("Bonjour monde !")

    Si tu as seulement besoin d'un objet Doc tokenisé,
    tu peux utiliser la méthode nlp.make_doc à la place,
    elle prend en argument un texte et retourne un doc.

    C'est aussi la manière dont spaCy le fait en coulisses :
    nlp.make_doc transforme le texte en un doc avant que les composants du pipeline ne soient appelés.

4 _ Désactivation de composants du pipeline
    spaCy te permet aussi de désactiver temporairement des composants du pipeline
    en utilisant le gestionnaire de contexte nlp.select_pipes.

    Il accepte les arguments nommés enable et disable qui peuvent
    définir une liste de chaînes de caractères indiquant les composants du pipeline à désactiver.
    Par exemple, si tu veux seulement utiliser l'entity recognizer pour traiter un document,
    tu peux désactiver temporairement le tagger et le parser.

    Après le bloc with, les composants de pipeline désactivés sont automatiquement réactivés.

    Dans le bloc with, spaCy exécutera uniquement les composants restants.
"""
import spacy
from spacy.tokens import Doc

# Intégration de contexte
# Tu peux même ajouter les métadonnées de contexte à des attributs personnalisés.
# Dans cet exemple, nous déclarons deux extensions, id et numero_page, avec comme valeur par défaut None.
# Après avoir traité le texte et en prenant en compte le contexte,
# nous pouvons actualiser les extensions du doc avec nos métadonnées de contexte.

Doc.set_extension("id", default=None)
Doc.set_extension("numero_page", default=None)

data = [
    ("Ceci est un texte", {"id": 1, "numero_page": 15}),
    ("Et un autre texte", {"id": 2, "numero_page": 16}),
]

nlp = spacy.load("fr_core_news_sm")

for doc, context in nlp.pipe(data, as_tuples=True):
    doc._.id = context["id"]
    doc._.numero_page = context["numero_page"]

# Désactivation de composants du pipeline
# Utilise nlp.select_pipes pour désactiver temporairement un ou plusieurs composants
# Désactive le tagger et le parser
with nlp.select_pipes(disable=["tagger", "parser"]):
    # Traite le texte et affiche les entités
    doc = nlp("Ceci est un texte")
    print(doc.ents)
# Les réactive après le bloc with
# N'exécute que les composants restants
