# Wrapping up

## Mes nouvelles compétences Spacy

### Chapitre 1
**1. Extraction de caractéristiques linguistiques : partie de discours, dépendances, entités nommées**

  Dans le premier chapitre, j'ai appris comment extraire des caractéristiques linguistiques comme les étiquettes de partie de discours, les dépendances syntaxiques et les entités nommées.

**2. Travail avec des pipelines pré-entraînés**

  J'ai appris comment travailler avec des pipelines pré-entraînés.

**3. Recherche de mots et de phrases selon des règles de correspondance avec [Matcher](https://spacy.io/api/matcher) et [PhraseMatcher](https://spacy.io/api/phrasematcher)**

  J'ai appris à écrire des règles de correspondances puissantes pour extraire des mots et des phrases en utilisant le [matcher](https://demos.explosion.ai/matcher?) et le phrase matcher de spaCy.
  Un autre matcher à tester: le [DependencyMatcher](https://spacy.io/api/dependencymatcher).
  Mes questions:
  - Peut-on matcher le contexte gauche (look-behind)?
  - Peut-on matcher le contexte droit (look-ahead)?
  - Peut-on matcher des sous-groupes ($1, $2, $3 etc)?
    - ---> Bref est-ce que les regexp étendus fonctionnent et peuvent se combiner aux capacités du matcher.
    - ---> https://spacy.io/usage/rule-based-matching: When using the REGEX operator, keep in mind that it operates on single tokens
    - Donc non...
    MAIS! Dans ce genre de cas on peut faire appel à la librairie re.
  - LIMITE: on n'a forcément plus accès au token et son contenu.
  - Xelda me manque... car on pouvait faire du lookahead et lookbehind ET on pouvait matcher le lemme, le pos et tout ce qui a été extrait à chaque couche d'extraction.
  - Un outil qui n'est plus maintenu qui permet de faire un peu des 2: https://github.com/clips/pattern/wiki/pattern-search

  

### Chapitre 2

**1. Meilleures pratiques pour l'emploi des structures de données Doc, Token Span, Vocab, Lexeme**

  Le chapitre 2 était consacré à l'extraction d'informations, et j'ai appris comment travailler avec les structures de données, les Doc, Token et Span, ainsi qu'avec le Vocab et les entrées lexicales.

**2. Recherche de similarités sémantiques avec les vecteurs de mots**

  J'ai aussi utilisé spaCy pour prédire des similarités sémantiques en utilisant des vecteurs de mots.

### Chapitre 3

**1. Écriture de composants de pipeline avec des extensions d'attributs**

  Dans le chapitre 3, j'ai acquis des connaissances plus complètes sur le pipeline de spaCy, et j'ai appris à écrire mes propres composants de pipeline personnalisés qui modifient le doc.

**2. Changement d'échelle des pipelines spaCy pour les rendre rapides**

  J'également créé mes propres extensions d'attributs personnalisées pour des docs, des tokens et des spans, et j'ai appris à traiter des flux et à rendre des pipelines plus rapides.

### Chapitre 4

**1. Création de données d'entraînement pour les modèles statistiques de spaCy**

  Enfin, dans le chapitre 4, j'ai appris à entraîner et à actualiser les modèles statistiques de spaCy, spécifiquement l'entity recognizer.

**2. Entraînement et actualisation des modèles de réseaux de neurones de spaCy avec de nouvelles données**

  J'ai appris quelques trucs utiles sur la manière de créer des données d'entraînement, et sur la manière de concevoir ton schéma de labellisation pour obtenir les meilleurs résultats.
  
## D'autres choses à faire avec spaCy

- [Entraînement et actualisation](https://spacy.io/usage/training) d'autres composants de pipeline
  - Etiqueteur de partie de discours
  - Analyseur de dépendances
  - Classificateur de texte (ne fait pas partie des modèles préentrainés, mais peut y être ajouté pour les compléter)
  - [Personnalisation du tokeniseur](https://spacy.io/usage/linguistic-features#tokenization)
    - Ajout de règles et d'exceptions pour scinder différemment le texte: on n'est pas obligé d'accepter la tokenisation tel quel, on peut l'adapter
  - [Ajout ou amélioration du support pour d'autres langues](https://spacy.io/usage/linguistic-features)
    - Plus de 60 langues actuellement
    - Marge de progression importante pour des améliorations et plus de langues
    - Possibilité d'entraîner des modèles pour d'autres langues

## A étudier: Spacy Projects

[Spacy Projects](https://github.com/explosion/projects) permet de gérer et de partager des workflows spaCy de bout en bout pour différents cas d'utilisation et domaines, et d'orchestrer l'entrainement, le packaging et le déploiement de pipelines personnalisés. On peut commencer par cloner un modèle de projet prédéfini, l'adapter à nos besoins, charger nos données, former un pipeline, l'exporter sous forme de package Python, télécharger nos résultats vers un stockage distant et partager nos résultats avec notre équipe.

### 🗃 Categories

| Name                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`pipelines`](https://github.com/explosion/projects/tree/v3/pipelines)       | Templates pour l'entraînement des pipelines NLP avec différents composants sur différents corpus.                                                                                                                                                                                                                                                                                    |
| [`tutorials`](https://github.com/explosion/projects/tree/v3/tutorials)       | Templates qui traitent de bout en bout un cas d'utilisation NLP spécifique. Notamment: [ner_double](https://github.com/explosion/projects/tree/v3/tutorials/ner_double) pour la gestion de pipelines avec 2 modèles ner et [ner_drugs](https://github.com/explosion/projects/tree/v3/tutorials/ner_drugs) un projet montrant la synergie possible entre prodigy pour annoter et spacy|
| [`integrations`](https://github.com/explosion/projects/tree/v3/integrations) | Templates présentant des intégrations avec des bibliothèques et des outils tiers pour la gestion de nos données et de nos expériences, l'itération sur des démos et des prototypes et l'envoi de nos modèles en production.                                                                                                                                                          |
| [`benchmarks`](https://github.com/explosion/projects/tree/v3/benchmarks)     | Templates pour reproduire les critères de référence de Spacy et produire des résultats quantifiables faciles à comparer avec d'autres systèmes ou versions de spaCy                                                                                                                                                                                                                  |
| [`experimental`](https://github.com/explosion/projects/tree/v3/experimental) | Workflows expérimentaux et autres travaux à la pointeà utiliser à nos risques et périls.                                                                                                                                                                                                                                                                                             |

Consulte le site web pour plus d'info et la documentation

👉 [spacy.io](https://spacy.io)

Merci et à bientôt ! 👋

