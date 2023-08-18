"""
Je vais tester l'étendu des capacités du matcher.

Mes questions:
    _ Peut-on matcher le contexte gauche (look-behind)?
    _ Peut-on matcher le contexte droit (look-ahead)?
    _ Peut-on matcher des sous-groupes ($1, $2, $3 etc)?
    ---> Bref est-ce que les regexp étendus fonctionnent et peuvent se combiner aux capacités du matcher.
    ---> https://spacy.io/usage/rule-based-matching: When using the REGEX operator, keep in mind that it operates on single tokens
    Donc non...
    MAIS! Dans ce genre de cas on peut faire appel à la librairie re.
        import spacy
        import re

        nlp = spacy.load("en_core_web_sm")
        doc = nlp("The United States of America (USA) are commonly known as the United States (U.S. or US) or America.")

        expression = r"[Uu](nited|\.?) ?[Ss](tates|\.?)"
        for match in re.finditer(expression, doc.text):
            start, end = match.span()
            span = doc.char_span(start, end)
            # This is a Span object or None if match doesn't map to valid token sequence
            if span is not None:
                print("Found match:", span.text)

    LIMITE: on n'a forcément plus accès au token et son contenu.
    Xelda me manque... car on pouvait faire du lookahead et lookbehind ET on pouvait matcher le lemme,
    le pos et tout ce qui a été extrait à chaque couche d'extraction.

    Un outil qui n'est plus maintenu qui permet de faire un peu des 2: https://github.com/clips/pattern/wiki/pattern-search

Un outil d'analyse des patterns Spacy: https://demos.explosion.ai/matcher

"""
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
# Add match ID "HelloWorld" with no callback and one pattern
pattern = [{"LOWER": "the"}, {"LOWER": "worldo"}]
pattern_r = [{"TEXT": {"REGEX": "friend"}}]
matcher.add("HelloWorld", [pattern])
matcher.add("Regexp", [pattern_r])
matcher.add("test-rule", [[{"LOWER": {"REGEX": "(?=the)"}}]], on_match=None)

patterns = [
    [{"LOWER": "hello"}, {"IS_PUNCT": True}, {"LOWER": "world"}],
    [{"LOWER": "hello"}, {"LOWER": "world"}],
]
matcher.add("HelloWorld", patterns)

doc = nlp("Hello, world! Hello world! THE WORLDO! Charlie is my best friend you know!")
matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    print(match_id, string_id, start, end, span.text)

print(f"{'TEXT':<12}{'POS':<10}{'DEP':<10}{'HEAD_TEXT':<10}{'HEAD_POS':<10}")
for token in doc:
    # Obtiens le texte du token, sa partie de discours et sa relation de dépendance
    token_text = token.text
    token_pos = token.pos_
    token_dep = token.dep_
    token_head = token.head
    token_head_pos = token_head.pos_
    token_head_text = token.head.text
    lefts = [(t.text, t.pos_) for t in token.lefts]
    rights = [(t.text, t.pos_) for t in token.rights]
    # Ceci sert uniquement au formatage de l'affichage
    print(
        f"{token_text:<12}{token_pos:<10}{token_dep:<10}{token_head_text:<10}{token_head_pos:<10}"
    )
