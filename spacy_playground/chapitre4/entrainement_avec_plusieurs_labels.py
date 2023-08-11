"""
Entrainement avec plusieurs labels

Voici un petit échantillon d’un jeu de données créé pour entraîner un nouveau type d’entité "SITE_WEB".
Le jeu de données original contient quelques milliers de phrases.
Dans cet exercice, tu vas effectuer la labellisation à la main.
En situation réelle, tu l’automatiserais probablement en utilisant un outil d’annotations -
par exemple, Brat, une solution open-source populaire,
ou Prodigy, notre propre outil d’annotations qui s’intègre avec spaCy.

Partie 1
Complète les positions des tokens pour les entités "SITE_WEB" dans les données.

Partie 2
    Un modèle a été entraîné avec les données que tu viens d’étiqueter,
    plus quelques milliers d’autres exemples.
    Après l’entraînement, il fait de l’excellent travail sur "SITE_WEB",
    mais ne reconnaît plus "PER". À quoi cela pourrait-il être dû ?

    R: Les données entraînement ne comportaient aucun exemple de "PER",
    donc le modèle a appris que ce label est incorrect.

Partie 3
Actualise les données d’entraînement pour inclure des annotations pour les entités "PER" “PewDiePie” et “Alexis Ohanian”.

"""
import spacy
from spacy.tokens import Span

nlp = spacy.blank("fr")

doc1 = nlp("Reddit noue un partenariat avec Patreon pour aider les créateurs à former des communautés")
doc1.ents = [
    Span(doc1, 0, 1, label="SITE_WEB"),
    Span(doc1, 5, 6, label="SITE_WEB"),
]

doc2 = nlp("PewDiePie explose le record de YouTube")
doc2.ents = [Span(doc2, 0, 1, label="PER"), Span(doc2, 5, 6, label="SITE_WEB")]

doc3 = nlp("Le fondateur de Reddit Alexis Ohanian a donné deux billets pour Metallica à des fans")
doc3.ents = [Span(doc3, 3, 4, label="SITE_WEB"), Span(doc3, 4, 6, label="PER")]

print("Done")
