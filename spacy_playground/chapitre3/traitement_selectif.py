"""
Traitement Sélectif

Dans cet exercice, tu vas utiliser les méthodes nlp.make_doc et nlp.select_pipes
pour appliquer uniquement les composants sélectionnés lors du traitement d’un texte.

Partie 1
Réécris le code en utilisant nlp.make_doc pour uniquement tokeniser le texte.

Partie 2
Désactive le parser et le lemmatizer en utilisant la méthode nlp.select_pipes.
Traite le texte et affiche toutes les entités contenues dans le doc.

"""
import spacy

nlp = spacy.load("fr_core_news_sm")
text = (
    "Le groupe aéronautique Airbus construit des avions et des "
    "hélicoptères vendus dans le monde entier. Le siège opérationnel du "
    "groupe est situé en France à Toulouse dans la région Occitanie."
)

# Tokenise seulement le texte
# doc = nlp(text)
doc = nlp.make_doc(text)
print([token.text for token in doc])

# Désactive le parser et le lemmatizer
with nlp.select_pipes(disable=["parser", "lemmatizer"]):
    # Traite le texte
    doc = nlp(text)
    # Affiche les entités du doc
    print(doc.ents)

# Maintenant que tu as pratiqué les trucs et astuces de performance,
# tu es prêt pour le chapitre suivant et entraîner les modèles de
# réseaux de neurones de spaCy.
