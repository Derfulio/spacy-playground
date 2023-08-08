"""
Prise en main

"""
# Importe spaCy
import spacy

# Crée un objet nlp français vide
nlp = spacy.blank("fr")

#contient le pipeline de traitement
#inclut des règles spécifiques à la langue pour la tokenisation etc.

# Créé en traitant une chaine de caractères avec l'objet nlp
doc = nlp("Bonjour monde !")

# Itère sur les tokens dans un Doc
# Un doc est représenté par une suite de tokens
for token in doc:
    print(token.text)

# L'objet Token
# Utilisation d'un indice au sein du Doc pour obtenir un Token unique
token = doc[1]

# Obtiens le texte du token avec l'attribut .text
print(token.text)

#L'objet Span

# Une portion du Doc est un objet Span
span = doc[1:3]

# Obtiens le texte du span avec l'attribut .text
print(span.text)

# Attributs lexicaux
# Traite un texte
doc = nlp("Cela coûte 5 €.")

# Plusieurs attributs sont rattachés au token
print("Index :   ", [token.i for token in doc])
print("Text :    ", [token.text for token in doc])

print("is_alpha :", [token.is_alpha for token in doc])
print("is_punct :", [token.is_punct for token in doc])
print("like_num :", [token.like_num for token in doc])

# Affiche le texte du document
print(doc.text)

# Crée l'objet nlp anglais
nlp = spacy.blank("en")

# Traite un texte (il signifie "Ceci est une phrase" en anglais)
doc = nlp("This is a sentence.")

# Affiche le texte du document
print(doc.text)

# Importe spaCy
import spacy

# Crée l'objet nlp espagnol
nlp = spacy.blank("es")

# Traite un texte (il signifie "Comment vas-tu ?" en espagnol)
doc = nlp("¿Cómo estás?")

# Affiche le texte du document
print(doc.text)