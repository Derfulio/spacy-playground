import spacy
from spacy.language import Language
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span


# Définis le composant personnalisé
@Language.component("length_component")
def length_component_function(doc):
    # Obtiens la longueur du doc
    doc_length = len(doc)
    print(f"Ce document comporte {doc_length} tokens.")
    # Retourne le doc
    return doc


# Charge le petit pipeline français
nlp = spacy.load("fr_core_news_sm")

# Ajoute le composant en premier dans le pipeline
# et affiche les noms des composants
nlp.add_pipe("length_component", first=True)
print(nlp.pipe_names)

# Traite un texte
doc = nlp("Ceci est une phrase.")

nlp = spacy.load("fr_core_news_sm")
animals = ["Golden Retriever", "chat", "tortue", "Rattus norvegicus"]
animal_patterns = list(nlp.pipe(animals))
print("animal_patterns :", animal_patterns)
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMAL", animal_patterns)


# Définis le composant personnalisé
@Language.component("animal_component")
def animal_component_function(doc):
    # Applique le matcher au doc
    matches = matcher(doc)
    # Crée un Span pour chaque correpondance et assigne-lui le label "ANIMAL"
    spans = [Span(doc, start, end, label="ANIMAL") for match_id, start, end in matches]
    # Actualise doc.ents avec les spans en correspondance
    doc.ents = spans
    return doc


# Ajoute le composant au pipeline après le composant "ner"
nlp.add_pipe("animal_component", after="ner")
print(nlp.pipe_names)

# Traite le texte et affiche le texte et le label pour les doc.ents
doc = nlp("J'ai un chat et un Golden Retriever")
print([(ent.text, ent.label_) for ent in doc.ents])
