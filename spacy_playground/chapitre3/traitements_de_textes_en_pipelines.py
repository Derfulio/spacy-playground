"""
Traitements de textes en pipelines
Composants intégrés au pipeline
    Nom	--> Description	--> Crée
    tagger	--> Part-of-speech tagger	--> Token.tag, Token.pos
    parser	--> Dependency parser	--> Token.dep, Token.head, Doc.sents, Doc.noun_chunks
    ner	--> Named entity recognizer	--> Doc.ents, Token.ent_iob, Token.ent_type
    textcat	--> Text classifier	--> Doc.cats (désactivé par défaut)


"""
import spacy

nlp = spacy.load("fr_core_news_sm")

# Attributs de pipeline
# nlp.pipe_names: liste de noms des composants du pipeline
print(nlp.pipe_names)
# ['tok2vec', 'morphologizer', 'parser', 'attribute_ruler', 'lemmatizer', 'ner']

# nlp.pipeline : liste de tuples (name, component)
print(nlp.pipeline)
# [('tok2vec', <spacy.pipeline.tok2vec.Tok2Vec>),
# ('morphologizer', <spacy.pipeline.morphologizer.Morphologizer>),
# ('parser', <spacy.pipeline.dep_parser.DependencyParser>),
# ('attribute_ruler', <spacy.pipeline.attributeruler.AttributeRuler>),
# ('lemmatizer', <spacy.lang.fr.lemmatizer.FrenchLemmatizer>),
# ('ner', <spacy.pipeline.ner.EntityRecognizer>)]

# composants personnalisés
# Anatomie d'un composant (1)
# Fonction qui prend un doc, le modifie et le retourne
# Enregistré avec le décorateur Language.component
# Peut être ajouté avec la méthode nlp.add_pipe
from spacy import Language


# Définit un composant personnalisé
@Language.component("custom_component")
def custom_component_function(doc):
    # Effectue une action sur le doc ici
    # Affiche la longueur du doc
    print("Longueur du doc :", len(doc))
    # Retourne l'objet doc
    return doc


# Ajoute le composant en premier dans le pipeline
nlp.add_pipe("custom_component", first=True)
# Argument	Description	Exemple
# last	Si True, ajoute en dernier	nlp.add_pipe("component", last=True)
# first	Si True, ajoute en premier	nlp.add_pipe("component", first=True)
# before	Ajoute avant le composant	nlp.add_pipe("component", before="ner")
# after	Ajoute après le composant	nlp.add_pipe("component", after="tagger")

# Affiche les noms des composants du pipeline
print("Pipeline :", nlp.pipe_names)

# Traite un texte
doc = nlp("Bonjour monde !")
