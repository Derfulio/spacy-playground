"""
Correspondances avec des règles

Pourquoi pas simplement des expressions régulières ?
    - Recherche de correspondances sur les objets Doc, pas seulement sur les chaînes de caractères
    - Recherche de correspondances sur les tokens et les attributs des tokens
    - Utilisation des prédictions d'un modèle
    - Exemple : "capture" (verbe) vs. "capture" (nom)

Par rapport aux expressions régulières, le matcher fonctionne avec des objets Doc et Token et pas simplement avec des chaines de caractères.

Il est également plus flexible : tu peux rechercher des textes mais aussi d'autres attributs lexicaux.

Tu peux même écrire des règles qui utilisent les prédictions d'un modèle.

Par exemple, trouve le mot "capture" seulement si c'est un verbe, pas un nom.

"""
import spacy

# Motifs de correspondance
# Listes de dictionnaires, un par token

# Recherche de correspondances exactes des textes
#[{"TEXT": "iPhone"}, {"TEXT": "X"}]

# Recherche d'attributs lexicaux
# [{"LOWER": "iphone"}, {"LOWER": "x"}]

#Recherche de n'importe quel attribut des tokens
# [{"LEMMA": "acheter"}, {"POS": "DET"}, {"POS": "NOUN"}]

# Importe le Matcher
from spacy.matcher import Matcher

# Charge un pipeline et crée l'objet nlp
nlp = spacy.load("fr_core_news_sm")

# Initialise le matcher avec le vocabulaire partagé
matcher = Matcher(nlp.vocab)

# Ajoute le motif au matcher
pattern = [{"TEXT": "iPhone"}, {"TEXT": "12"}]
matcher.add("IPHONE_PATTERN", [pattern])

# Traite un texte
doc = nlp("La date de sortie du futur iPhone 12 a fuité")

# Appelle le matcher sur le doc
matches = matcher(doc)

# Quand tu appelles le matcher sur un doc, il retourne une liste de tuples.
#
# Chaque tuple contient trois valeurs : l'ID du motif, l'indice de début et l'indice de fin du span en correspondance.
#
# Cela signifie que nous pouvons itérer sur les correspondances et créer un objet Span : une portion du doc depuis
# l'indice de début jusqu'à l'indice de fin. Itère sur les correspondances
for match_id, start, end in matches:
    # Obtiens le span en correspondance
    matched_span = doc[start:end]
    print(matched_span.text)
    # match_id: valeur de hash du nom du motif
    # start: indice de début du span en correspondance
    # end: indice de fin du span en correspondance

# Voici un exemple de motif un peu plus complexe utilisant des attributs lexicaux.
pattern = [
    {"LOWER": "coupe"},
    {"LOWER": "du"},
    {"LOWER": "monde"},
    {"LOWER": "fifa"},
    {"IS_DIGIT": True},
    {"IS_PUNCT": True}
]
matcher.add("FIFA_PATTERN", [pattern])
doc = nlp("Coupe du Monde FIFA 2018 : la France a gagné !")
matches = matcher(doc)
for match_id, start, end in matches:
    # Obtiens le span en correspondance
    matched_span = doc[start:end]
    print(matched_span.text)

# Recherche sur d'autres attributs des tokens

# Un verbe avec le lemme "photographier", suivi par un déterminant et par un nom.

# Ce motif trouvera "photographiait les fleurs" et "photographiera les oiseaux".

pattern = [
    {"LEMMA": "photographier", "POS": "VERB"},#plusieurs critères sur un même token
    {"POS": "DET"},
    {"POS": "NOUN"}
]
matcher.add("PHOTO_PATTERN", [pattern])
doc = nlp("Avant elle photographiait les fleurs. Désormais elle photographiera les oiseaux.")
matches = matcher(doc)
for match_id, start, end in matches:
    # Obtiens le span en correspondance
    matched_span = doc[start:end]
    print(matched_span.text)

# Utilisation d'opérateurs et de quantificateurs
pattern = [
    {"LEMMA": "acheter", "POS": "VERB"},
    {"POS": "DET"},
    {"POS": "ADJ", "OP": "?"}, # optionnel : trouve 0 or 1 fois
    {"POS": "NOUN"}
]
matcher.add("OP_PATTERN_1", [pattern])
doc = nlp("J'ai acheté un nouveau smartphone. Maintenant j'achète des applis.")
matches = matcher(doc)
for match_id, start, end in matches:
    # Obtiens le span en correspondance
    matched_span = doc[start:end]
    print(matched_span.text)

# Exemple	Description
# {"OP": "!"}	Négation : trouve 0 fois
# {"OP": "?"}	Optionnel : trouve 0 ou 1 fois
# {"OP": "+"}	Trouve 1 ou plusieurs fois
# {"OP": "*"}	Trouve 0 ou plusieurs fois

doc = nlp("Apple : le nouveau modèle X Pro attendu pour l'été.")

# Initialise le matcher avec le vocabulaire partagé
matcher = Matcher(nlp.vocab)

# Crée un motif qui recherche les deux tokens : "X" et "Pro"
pattern = [{"TEXT": "X"}, {"TEXT": "Pro"}]

# Ajoute le motif au matcher
matcher.add("IPHONE_X_PATTERN", [pattern])

# Utilise le matcher sur le doc
matches = matcher(doc)
print("Résultats :", [doc[start:end].text for match_id, start, end in matches])

#  Ecriture des motifs de correspondance plus complexes qui utilisent différents attributs des tokens et des opérateurs.
doc = nlp(
    "Après avoir effectué la mise à jour d'iOS vous ne constaterez pas de "
    "renouveau radical : rien de commun avec le bouleversement que nous "
    "avions connu avec iOS 7. Globalement iOS 11 reste très semble à iOS 10. "
    "Mais vous découvrirez quelques changements en approfondissant un peu."
)

# Écris un motif des versions complètes d'iOS ("iOS 7", "iOS 11", "iOS 10")
pattern = [{"TEXT": "iOS"}, {"IS_DIGIT": True}]

# Ajoute le motif au matcher et applique le matcher au doc
matcher.add("IOS_VERSION_PATTERN", [pattern])
matches = matcher(doc)
print("Nombre de correspondances trouvées :", len(matches))

# Itère sur les correspondances et affiche la portion de texte
for match_id, start, end in matches:
    print("Correspondance trouvée :", doc[start:end].text)

doc = nlp(
    "j'ai téléchargé Fortnite sur mon ordinateur portable et je ne peux pas "
    "du tout lancer le jeu. Quelqu'un pour m'aider ? "
    "donc quand je téléchargeais Minecraft j'ai eu la version de Windows dans "
    "le dossier .zip et j'ai utilisé le programme par défaut pour le "
    "décompresser... est-ce qu'il faut aussi que je télécharge Winzip ?"
)

# Écris un motif qui recherche une forme de "télécharger" suivie d'un nom propre
pattern = [{"LEMMA": "télécharger"}, {"POS": "PROPN"}]

# Ajoute le motif au matcher et applique le matcher au doc
matcher.add("DOWNLOAD_THINGS_PATTERN", [pattern])
matches = matcher(doc)
print("Nombre de correspondances trouvées :", len(matches))

# Itère sur les correspondances et affiche la portion de texte
for match_id, start, end in matches:
    print("Correspondance trouvée :", doc[start:end].text)

doc = nlp(
    "L'appli se distingue par une interface magnifique, la recherche "
    "intelligente, la labellisation automatique et les réponses "
    "vocales fluides."
)

# Écris un motif pour un adjectif suivi d'un ou deux noms
pattern = [{"POS": "NOUN"}, {"POS": "ADJ"}, {"POS": "ADJ", "OP": "?"}]

# Ajoute le motif au matcher et applique le matcher au doc
matcher.add("ADJ_NOUN_PATTERN", [pattern])
matches = matcher(doc)
print("Nombre de correspondances trouvées :", len(matches))

# Itère sur les correspondances et affiche la portion de texte
for match_id, start, end in matches:
    print("Correspondance trouvée :", doc[start:end].text)