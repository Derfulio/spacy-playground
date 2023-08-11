"""
Source: https://stackoverflow.com/questions/59730960/convert-ner-spacy-format-to-iob-format
This is closely related to and mostly copied from https://stackoverflow.com/a/59209377/461847,
see the notes in the comments there, too.
NOTE: not working yet, maybe useless
"""
import spacy
from spacy.tokens import Doc, DocBin
from spacy.training import offsets_to_biluo_tags, biluo_to_iob, biluo_tags_to_offsets, biluo_tags_to_spans

TRAIN_DATA = [
    ("Qui est Shaka Khan?", {"entities": [(8, 18, "PERSON")]}),
    ("J'aime Londres et Berlin.", {"entities": [(7, 14, "LOC"), (18, 24, "LOC")]}),
]

nlp = spacy.load("fr_core_news_sm")

PIPES_TO_TRAIN = ["ner", "nerer", "whatever"] #Bah oui, si je veux les entrainer, je ne dois pas les avoir dans mon trainset
disabled_pipes = [pipe for pipe in PIPES_TO_TRAIN if pipe in nlp.pipe_names]

# Déclare l'extension de propriété de Doc "biluo"
Doc.set_extension("biluo", default=[])

# Déclare l'extension de propriété de Doc "iob"
Doc.set_extension("iob", default=[])

train_set = []
# Désactive l'extracteur d'entités nommées
with nlp.select_pipes(disable=disabled_pipes):
    # Traite le flux de documents
    for doc, annot in nlp.pipe(TRAIN_DATA, as_tuples=True):
        print(doc.ents)
        print([(ent.text, ent.label_) for ent in doc.ents])
        # Convert to biluo format
        tags = offsets_to_biluo_tags(doc, annot['entities'])
        doc._.biluo = tags
        print(tags)
        # Convert biluo to Span list and add to doc
        docents = biluo_tags_to_spans(doc, tags)
        # The way I understand set_ents arguments
        # entities: those I want to extract --> Correct
        # blocked: those I don't want to extract: "I don't want you to extract this, don't forget that" --> Incorrect
        # missing: those I know the span is incorrect, but I don't want to lose time to correct it --> Partially correct
        # outside: same as blocked I guess, but more like "there's nothing to see here, you can forget it" --> Outside
        # Note: I have nothing to say that the span is correct, not the type. Maybe I should create an "Unknown" tag to remember this by default
        # Note: To be able to have this level of distinction between tags is awesome! Would be great for a feedback loop
        doc.set_ents(entities=docents, blocked=[], missing=[], outside=[], default="outside")
        print(doc.ents)
        print([(ent.text, ent.label_) for ent in doc.ents])
        # then convert L->I and U->B to have IOB tags for the tokens in the doc
        tags = biluo_to_iob(tags)
        doc._.iob = tags
        print(tags)

        # Add doc to train_set
        train_set.append(doc)

train_bin = DocBin(docs=train_set)
train_bin.to_disk("./train_set.spacy")