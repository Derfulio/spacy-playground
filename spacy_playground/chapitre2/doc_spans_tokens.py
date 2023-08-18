"""
Doc

Le Doc est une des structures de données centrales de spaCy. Il est créé automatiquement quand tu traites un texte avec l'objet nlp. Mais tu peux aussi instancier la classe manuellement.

Après avoir créé l'objet nlp, nous pouvons importer la classe Doc à partir de spacy.tokens.

Ici nous créons un doc à partir de trois mots. Les espaces sont une liste de valeurs booléennes indiquant si le mot est suivi ou non par un espace. Chaque token inclut cette information - même le dernier !

La classe Doc requiert trois arguments : le vocabulaire partagé, les mots et les espaces.

Span

Un Span est une portion d'un document composé d'un ou de plusieurs tokens.
Le Span requiert trois arguments : le doc auquel il fait référence, et les indices de début et de fin du span.
N'oublie pas que l'indice de fin est exclu !

Pour créer un Span manuellement, nous pouvons aussi importer la classe à partir de spacy.tokens.
Nous pouvons ensuite l'instancier avec le doc et les indices de début et de fin du span, ainsi qu'avec un label optionnel.

Les doc.ents sont modifiables, donc nous pouvons ajouter manuellement des entités en les remplaçant par une liste de spans.
"""

# Crée un objet nlp
import spacy

nlp = spacy.blank("fr")

# Importe les classes Doc et Span
from spacy.tokens import Doc, Span

# Les mots et les espaces à partir desquels créer le doc
words = ["Bonjour", "monde", "!"]
spaces = [True, True, False]

# Crée un doc manuellement
doc = Doc(nlp.vocab, words=words, spaces=spaces)

# Crée un span manuellement
span = Span(doc, 0, 2)

# Crée un span avec un label
span_with_label = Span(doc, 0, 2, label="GREETING")

# Ajoute le span à doc.ents
doc.ents = [span_with_label]

# Doc et Span sont très puissants et contiennent les références et les relations entre les mots et les phrases
## Convertis les résultats en chaînes le plus tard possible
## Utilise les attributs des tokens quand ils existent – par exemple, token.i pour l'indice du token
# N'oublie pas de passer en argument le vocab partagé

# Texte désiré : "spaCy est cool."
words = ["spaCy", "est", "cool", "."]
spaces = [True, True, False, False]

# Crée un Doc à partir des mots et des espaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

# Texte désiré : "Allez, on commence !"
words = ["Allez", ",", "on", "commence", "!"]
spaces = [False, True, True, True, False]

# Crée un Doc à partir des mots et des espaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

# Texte désiré : "Oh, vraiment ?!"
words = ["Oh", ",", "vraiment", "?", "!"]
spaces = [False, True, True, True, False]

# Crée un Doc à partir des mots et des espaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

words = ["Elle", "aime", "David", "Bowie"]
spaces = [True, True, True, False]

# Crée un doc à partir des mots et des espaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

# Crée un span pour "David Bowie" à partir du doc
# et assigne-lui le label "PER"
span = Span(doc, 2, 4, label="PER")
print(span.text, span.label_)

# Ajoute le span aux entités du doc
doc.ents = [span]

# Affiche les textes et les labels des entités
print([(ent.text, ent.label_) for ent in doc.ents])

#  Savoir créer manuellement des objets de spaCy et modifier
# les entités sera utile plus tard quand tu créeras tes propres pipelines
# d'extraction d'informations.

nlp = spacy.load("fr_core_news_sm")
doc = nlp("Berlin semble être une jolie ville")

for token in doc:
    # Vérifie si le token courant est un nom propre
    if token.pos_ == "PROPN":
        # Vérifie si le token suivant est un verbe
        if token.i + 1 < len(doc) and doc[token.i + 1].pos_ == "VERB":
            result = token.text
            print("Trouvé un nom propre avant un verbe :", result)

# Si la solution fonctionne bien ici pour l'exemple
# donné, il y a encore des choses qui peuvent être améliorées. Si le doc se
# termine par un nom propre, doc[token.i + 1] va générer une erreur. Pour être
# certain de pouvoir généraliser, tu devrais d'abord vérifier si token.i + 1 <
# len(doc).
