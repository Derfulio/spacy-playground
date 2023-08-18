"""
Vecteurs de mots et similarité sémantique
Objectif:
Dans cette leçon, tu vas apprendre à utiliser spaCy pour prédire à quel point des documents,
des spans ou des tokens sont similaires les uns avec les autres.

Vecteurs de mots et similarité sémantique
Comparaison de similarité sémantique
    - spaCy peut comparer deux objets et prédire leur similarité
    - Doc.similarity(), Span.similarity() et Token.similarity()
    - Accepte un autre objet et retourne un score de similarité (de 0 à 1)
    - Important : nécessite un pipeline qui inclut les vecteurs de mots, par exemple:
        ✅ fr_core_news_md (moyen)
        ✅ fr_core_news_lg (grand)
        🚫 PAS fr_core_news_sm (petit)
"""
import spacy

# Charge un plus grand pipeline avec les vecteurs
nlp = spacy.load("fr_core_news_md")

# Compare deux documents
doc1 = nlp("J'aime la pizza")
doc2 = nlp("J'aime la quiche lorraine")
print(doc1.similarity(doc2))
# Ici, la prédiction est un score plutôt élevé de similarité de 0,96 pour "J'aime la pizza" et "J'aime la quiche lorraine".
# 0.9686798359892211

# Cela fonctionne aussi avec les tokens.

# Compare deux tokens
doc = nlp("J'aime la pizza et la quiche")
token1 = doc[3]
token2 = doc[6]
print(token1.similarity(token2))
# Selon les vecteurs de mots, les tokens "pizza" et "quiche" sont relativement similaires, et obtiennent un score de 0,62.
# 0.62105

# Compare un document avec un token
doc = nlp("J'aime la pizza")
token = nlp("savon")[0]
# Ici, le score de similarité est assez bas et les deux objets sont considérés assez peu similaires.
print(doc.similarity(token))
# 0.12344265753392583

# Compare un span avec un document
span = nlp("J'aime la pizza et les pâtes")[3:7]
doc = nlp("McDonalds vend des hamburgers")
# Le score retourné ici est 0,62, donc il y a une forme de similarité.
print(span.similarity(doc))
# 0.6186440160069984

# Comment spaCy prédit la similarité ?
## La similarité est déterminée en utilisant des vecteurs de mots
## Des représentations multi-dimensionnelles de la signification des mots
## Générées avec un algorithme comme Word2Vec et beaucoup de textes
## Peuvent être ajoutés aux pipelines de spaCy
## Par défaut : similarité cosinus, mais peut être modifiée
## Les vecteurs des Doc et Span sont par défaut la moyenne des vecteurs des tokens
## Les phrases courtes sont meilleures que les longs documents comportant de nombreux mots non pertinents

doc = nlp("J'ai une banane")
# Accède au vecteur via l'attribut token.vector
print(doc[3].vector)
# Pour se faire une idée, voici un exemple montrant à quoi ressemblent ces vecteurs.
# D'abord, nous chargeons à nouveau le pipeline moyen, qui comporte des vecteurs de mots.
# Ensuite, nous pouvons traiter un texte et chercher le vecteur d'un token en utilisant l'attribut .vector.
# Le résultat est un vecteur à 300 dimensions du mot "banane".

# La similarité depend du contexte d'application
# Utile pour de nombreuses applications : systèmes de recommandations, repérage de doublons etc.
# Il n'y a pas de définition objective de "similarité"
# Cela dépend du contexte et des besoins de l'application
doc1 = nlp("J'aime les chats")
doc2 = nlp("Je déteste les chats")

print(doc1.similarity(doc2))
# Les vecteurs de mots de spaCy attribuent par défaut un score élevé de similarité entre
# "J'aime les chats" et "Je déteste les chats".
# Cela parait logique, car les deux textes expriment des sentiments à propos des chats.
# Mais dans un contexte d'application différent,
# tu pourrais vouloir considérer les phrases comme étant très dissemblables,
# parce qu'elles expriment des sentiments opposés.

# Traite le texte
doc = nlp("Deux bananes en pyjamas")

# Obtiens le vecteur pour le token "bananes"
bananas_vector = doc[1].vector
print(bananas_vector)

doc1 = nlp("Le temps est au beau fixe")
doc2 = nlp("Le ciel est clair")

# Obtiens la similarité entre doc1 et doc2
similarity = doc1.similarity(doc2)
print(similarity)

doc = nlp("télé et livres")
token1, token2 = doc[0], doc[2]

# Obtiens la similarité entre les tokens "télé" et "livres"
similarity = token1.similarity(token2)
print(similarity)

doc = nlp(
    "C'était un super restaurant. Ensuite nous sommes allés dans un bar vraiment sympa."
)

# Crée des spans pour "super restaurant" et "bar vraiment sympa"
span1 = doc[3:5]
span2 = doc[12:15]

# Obtiens la similarité entre les spans
similarity = span1.similarity(span2)
print(similarity)

# Les similarités ne sont pas *toujours* aussi
# probantes. Si tu commences à développer sérieusement des applications de NLP qui
# exploitent la similarité sémantique, tu pourrais vouloir entrainer des vecteurs
# sur tes propres données,ou ajuster l'algorithme de similarité sémantique.
