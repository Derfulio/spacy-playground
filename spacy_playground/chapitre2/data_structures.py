"""
Vocabulaire, lexèmes et magasin de chaînes

Vocabulaire partagé et magasin de chaînes
    - Vocab : stocke les données partagées entre des documents multiples
    - Pour économiser de l'espace mémoire, spaCy encode toutes les chaînes en valeurs de hachage
    - Les chaînes ne sont stockées qu'une seule fois dans le StringStore via nlp.vocab.strings
    - String store : table de consultation dans les deux sens
nlp.vocab.strings.add("souvent")
souvent_hash = nlp.vocab.strings["souvent"]
souvent_string = nlp.vocab.strings[souvent_hash]

    - Les hashs ne peuvent pas être inversés – c'est pourquoi nous avons besoin de fournir le vocabulaire partagé
# Génère une erreur si nous n'avons pas déjà vu la chaîne avant
string = nlp.vocab.strings[821433950267086228]
"""
import spacy

nlp = spacy.load("fr_core_news_sm")

# Recherche de la chaîne et du hash dans nlp.vocab.strings
doc = nlp("Ines nage souvent")
print("valeur de hash :", nlp.vocab.strings["souvent"])
print("valeur de chaîne :", nlp.vocab.strings[821433950267086228])
# valeur de hash : 821433950267086228
# valeur de chaîne : souvent
# Le doc expose aussi le vocabulaire et les chaînes

doc = nlp("Ines nage souvent")
print("valeur de hash :", doc.vocab.strings["souvent"])
# valeur de hash : 821433950267086228

# Lexèmes : éléments du vocabulaire

# Les lexèmes sont des éléments du vocabulaire indépendants du contexte.

# Tu peux obtenir un lexème en cherchant une chaîne ou un ID de hash dans le vocabulaire.

# Les lexèmes exposent des attributs, tout comme les tokens.

# Un objet Lexeme est un élément du vocabulaire
doc = nlp("Ines nage souvent")
lexeme = nlp.vocab["souvent"]

# Affiche les attributs lexicaux
print(lexeme.text, lexeme.orth, lexeme.is_alpha)
# souvent 821433950267086228 True
# Contient les informations indépendantes du contexte à propos d'un mot
# Le texte du mot : lexeme.text et lexeme.orth (le hash)
# Des attributs lexicaux comme lexeme.is_alpha
# Etiquettes de partie de discours non dépendantes du contexte, dépendances ou labels d'entités
