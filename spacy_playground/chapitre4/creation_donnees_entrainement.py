"""
Création de données d'entrainement

1_
    Le Matcher basé sur les règles de spaCy est un excellent moyen
    pour créer rapidement des données d’entraînement pour les modèles d’entités nommées.
    Une liste de phrases est accessible via la variable TEXTS. Tu peux l’imprimer pour l’inspecter.
    Nous voulons trouver toutes les mentions de différents modèles d’iPhone,
    donc nous allons créer des données d’entraînement pour apprendre à notre modèle à les reconnaître en tant que "GADGET".

    Écris un motif pour deux tokens dont la forme en minuscules correspond à "iphone" et "x".
    Écris un motif pour deux tokens : un token dont la forme en minuscules correspond à "iphone" et un nombre.

2_
    Après avoir créé les données pour notre corpus, nous devons les sauvegarder dans un fichier .spacy.
    Le code de l’exemple précédent est déjà fourni.

    Instancie le DocBin avec la liste des docs.
    Sauve le DocBin dans un fichier appelé train.spacy.

"""

TEXTS = [
    "Comment précommander l'iPhone X",
    "l'iPhone X arrive",
    "Dois-je dépenser 1.000 € pour l'iPhone X ?",
    "Les tests de l'iPhone 8 sont là",
    "iPhone 11 contre iPhone 8 : quelles sont les différences ?",
    "Il me faut un nouveau téléphone ! Des suggestions à me faire ?",
]

import json
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span, DocBin

# with open("exercises/fr/iphone.json", encoding="utf8") as f:
#   TEXTS = json.loads(f.read())

nlp = spacy.blank("fr")
matcher = Matcher(nlp.vocab)

# Deux tokens dont les formes majuscules correspondent à "iphone" et "x"
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]

# Tokens dont les formes majuscules correspondent à "iphone" et un nombre
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]

# Ajoute les motifs au matcher et crée des docs avec les entités en correspondance
matcher.add("GADGET", [pattern1, pattern2])
docs = []
for doc in nlp.pipe(TEXTS):
    matches = matcher(doc)
    spans = [Span(doc, start, end, label=match_id) for match_id, start, end in matches]
    print(spans)
    doc.ents = spans
    docs.append(doc)

doc_bin = DocBin(docs=docs)
doc_bin.to_disk("./train.spacy")
