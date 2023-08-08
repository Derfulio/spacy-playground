"""
Documents, Spans et tokens
Quand tu passes une chaîne de caractères à un objet nlp,
spaCy commence par découper le texte en tokens et crée un objet document.
Dans cet exercice, tu vas en apprendre davantage sur le Doc, ainsi que sur ses vues Token et Span.

"""

# Importe spacy et crée l'objet nlp français
import spacy

nlp = spacy.blank("fr")

# Traite le texte
doc = nlp("La forêt est peuplée de loups gris et renards roux.")

# Sélectionne le premier token
first_token = doc[0]

# Affiche le texte du premier token
print(first_token.text)

# Importe spacy et crée l'objet nlp français
import spacy

nlp = spacy.blank("fr")

# Traite le texte
doc = nlp("La forêt est peuplée de loups gris et renards roux.")

# La portion du Doc pour "loups gris"
loups_gris = doc[5:7]
print(loups_gris.text)

# La portion du Doc pour "loups gris et renards roux" (sans le ".")
loups_gris_et_renards_roux = doc[5:10]
print(loups_gris_et_renards_roux.text)

text = "Apple : le nouveau modèle X Pro attendu pour l'été."

# Traite le texte
doc = nlp(text)

# Itère sur les entités
for ent in doc.ents:
    # Affiche le texte de l'entité et son label
    print(ent.text, ent.label_)

# Obtiens la portion pour "X Pro"
x_pro = doc[5:7]

# Affiche la portion de texte
print("Entité manquante :", x_pro.text)