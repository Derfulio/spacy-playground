"""
Attributs étendus
Comment ajouter des attributs personnalisés aux objets Doc, Token et Span pour stocker des données personnalisées.

Ajoute des métadonnées personnalisées aux documents, tokens et spans
Accessible via la propriété ._

doc._.title = "Mon document"
token._.is_color = True
span._.has_color = False

Déclaré sur les classes globales Doc, Token ou Span en utilisant la méthode set_extension

# Importe les classes globales
from spacy.tokens import Doc, Token, Span

# Définit des extensions sur Doc, Token et Span
Doc.set_extension("title", default=None)
Token.set_extension("is_color", default=False)
Span.set_extension("has_color", default=False)

Types d'attributs étendus
_ Extensions d'attributs
_ Extensions de propriétés
_ Extensions de méthodes

"""
import spacy

# Extensions d'attributs
# Définit une valeur par défaut qui peut être modifiée
from spacy.tokens import Token

nlp = spacy.blank("fr")

# Définit l'extension sur le Token avec une valeur par défaut
Token.set_extension("is_color", default=False)

doc = nlp("Le ciel est bleu.")

# Modifie la valeur de l'attribut étendu
doc[3]._.is_color = True

# Plusieurs attributs sont rattachés au token
print("Index :   ", [token.i for token in doc])
print("Text :    ", [token.text for token in doc])
print("Color :    ", [token._.is_color for token in doc])


# Extensions de propriétés
# Définit une fonction getter et une fonction optionnelle setter
# Le getter n'est appelé que quand tu récupères la valeur de l'attribut


# Définit la fonction getter
def get_is_color(token):
    colors = ["rouge", "jaune", "bleu"]
    return token.text in colors


# Définit l'extension de Token avec le getter
Token.set_extension("is_color", getter=get_is_color, force=True)

doc = nlp("Le ciel est bleu.")
print(doc[3]._.is_color, "-", doc[3].text)

# Les extensions de Span devraient presque toujours utiliser un getter
from spacy.tokens import Span


# Définit la fonction getter
def get_has_color(span):
    colors = ["rouge", "jaune", "bleu"]
    return any(token.text in colors for token in span)


# Définit l'extension de Span avec le getter
Span.set_extension("has_color", getter=get_has_color)

doc = nlp("Le ciel est bleu.")
print(doc[1:4]._.has_color, "-", doc[1:4].text)
print(doc[0:2]._.has_color, "-", doc[0:2].text)

# Extensions de méthodes
# Assigne une fonction qui devient accessible en tant que méthode de l'objet
# Te permet de passer des arguments à la fonction d'extension
from spacy.tokens import Doc


# Définit la méthode avec des arguments
def has_token(doc, token_text):
    in_doc = token_text in [token.text for token in doc]
    return in_doc


# Définit l'extension du Doc avec la méthode
Doc.set_extension("has_token", method=has_token)

doc = nlp("Le ciel est bleu.")
print(doc._.has_token("bleu"), "- bleu")
print(doc._.has_token("nuage"), "- nuage")

# Déclare l'extension d'attribut de Token "is_country"
# avec la valeur par défaut False
Token.set_extension("is_country", default=False)

# Traite le texte et définis l'attribut is_country à True pour le token "Suisse"
doc = nlp("J'habite en Suisse.")
doc[3]._.is_country = True

# Affiche le texte du token et l'attribut is_country pour tous les tokens
print([(token.text, token._.is_country) for token in doc])


# Définis la fonction getter qui prend en argument un token
# et retourne son texte inversé
def get_reversed(token):
    return token.text[::-1]


# Déclare l'extension de propriété de Token "reversed"
# avec le getter get_reversed
Token.set_extension("reversed", getter=get_reversed)

# Traite le texte et affiche l'attribut inversé pour chaque token
doc = nlp("Toutes les généralisations sont fausses, celle-ci aussi.")
for token in doc:
    print("reversed :", token._.reversed)

# Attributs étendus


# Définis la fonction getter
def get_has_number(doc):
    # Retourne si un token quelconque du doc renvoie True pour token.like_num
    return any(token.like_num for token in doc)


# Déclare l'extension de propriété de Doc "has_number"
# avec le getter get_has_number
Doc.set_extension("has_number", getter=get_has_number)

# Traite le texte et vérifie l'attribut personnalisé has_number
doc = nlp("Le musée a fermé pour cinq ans en 2012.")
print("has_number :", doc._.has_number)

# Les méthodes étendues peuvent accepter un ou plusieurs arguments.
# Par exemple : doc._.some_method("argument").
# Le premier argument passé à la méthode est toujours le Doc,
# le Token ou le Span sur lequel la méthode a été appelée.


# Définis la méthode
def to_html(span, tag):
    # Entoure le texte du span avec une balise HTML et retourne l'ensemble
    return f"<{tag}>{span.text}</{tag}>"


# Déclare l'extension de méthode de Span "to_html" avec la méthode to_html
Span.set_extension("to_html", method=to_html)

# Traite le texte et applique la méthode to_html sur le span
# avec la balise "strong"
doc = nlp("Bonjour monde, ceci est une phrase.")
span = doc[0:2]
print(span._.to_html("strong"))
