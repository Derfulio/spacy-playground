import spacy

nlp = spacy.blank("fr")
doc = nlp("J'ai un chat")

# Recherche le hash pour le mot "chat"
cat_hash = nlp.vocab.strings["chat"]
print(cat_hash)

# Recherche cat_hash pour obtenir la chaine
cat_string = nlp.vocab.strings[cat_hash]
print(cat_string)


doc = nlp("David Bowie a le label PER")

# Cherche le hash pour le label de chaine "PER"
person_hash = nlp.vocab.strings["PER"]
print(person_hash)

# Cherche person_hash pour obtenir la chaine
person_string = nlp.vocab.strings[person_hash]
print(person_string)
