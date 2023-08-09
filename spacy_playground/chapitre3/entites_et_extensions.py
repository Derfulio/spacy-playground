"""
Entités et extensions
Dans cet exercice, tu vas combiner l’extension d’attributs personnalisés avec les prédictions statistiques
et créer un accesseur d’attribut qui retourne une URL de recherche Wikipédia si le span est une personne,
une organisation ou un lieu.

Complète le getter get_wikipedia_url pour qu’il retourne une URL
uniquement si le label du span est dans la liste des labels.
Définis l’extension de Span nommée "wikipedia_url" avec le getter get_wikipedia_url.
Itère sur les entités du doc et affiche leur URL Wikipédia.
"""
import spacy
from spacy.tokens import Span

nlp = spacy.load("fr_core_news_sm")


def get_wikipedia_url(span):
    # Retourne une URL Wikipédia si le span possède un des libellés
    if span.label_ in ("PER", "ORG", "GPE", "LOCATION"):
        entity_text = span.text.replace(" ", "_")
        return "https://fr.wikipedia.org/w/index.php?search=" + entity_text


# Définis l'extension de Span wikipedia_url avec le getter get_wikipedia_url
Span.set_extension("wikipedia_url", getter=get_wikipedia_url)

doc = nlp(
    "Pendant plus de cinquante ans depuis ses tout premiers enregistrements "
    "jusqu'à son dernier album, David Bowie a toujours été à l'avant-garde "
    "de la culture contemporaine."
)
for ent in doc.ents:
    # Affiche le text et l'URL Wikipédia de l'entité
    print(ent.text, ent._.wikipedia_url)

# Maintenant tu as un composant de pipeline qui utilise des
# entités nommées prédites par le modèle pour générer des URL Wikipédia et les
# ajouter comme attribut personnalisé. Essaie d'ouvrir le lien dans ton navigateur
# pour voir ce qui se passe !