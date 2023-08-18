"""
Entrainement avec plusieurs labels

Voici un petit échantillon d’un jeu de données créé pour entraîner un nouveau type d’entité "SITE_WEB".
Le jeu de données original contient quelques milliers de phrases.
Dans cet exercice, tu vas effectuer la labellisation à la main.
En situation réelle, tu l’automatiserais probablement en utilisant un outil d’annotations - par exemple,
Brat, une solution open-source populaire (http://brat.nlplab.org/),
ou Prodigy, notre propre outil d’annotations qui s’intègre avec spaCy (https://prodi.gy/).

Autres alternatives: (https://github.com/topics/data-labeling)
    _ A list: https://github.com/HumanSignal/awesome-data-labeling
    _ https://github.com/doccano/doccano
        --> Python client: https://github.com/doccano/doccano-client
        --> Competitor List: https://github.com/doccano/awesome-annotation-tools
    _ https://github.com/HumanSignal/label-studio
        --> See also https://github.com/HumanSignal/label-studio-transformers
    _ https://github.com/cleanlab/cleanlab
    _ https://github.com/jiesutd/YEDDA
    _ https://github.com/falcony-io/ml-annotate
    _ https://github.com/d5555/TagEditor --> Desktop App fully compatible with Spacy
    _ https://github.com/RTIInternational/SMART
    _ https://github.com/etalab/piaf --> En mode gamification (questions/réponses)
        --> C'est français, proposé par l'Etalab (https://piaf.etalab.studio/)
        --> L’ambition du projet PIAF est de construire ce(s) jeu(x) de données francophones pour l’IA de manière ouverte et contributive
    _ https://github.com/code-kern-ai/refinery --> Très complet et prometteur, à tester
    _ https://github.com/dataqa/nlp-labelling
    _ https://github.com/samueldobbie/markup
    _ https://github.com/CyberAgent/fast-annotation-tool
        --> To create mobile phone annotation tool
    _ https://www.johnsnowlabs.com/nlp-lab/ --> Seems good, but fishy (free? not free?)
    _ https://www.lighttag.io/ --> Free for 1 user

 Dataset generator: https://github.com/infinitylogesh/mutate
 A étudier: https://support.prodi.gy/t/prodigy-annotation-manager-update-prodigy-scale-prodigy-teams/805
    https://prodi.gy/

Partie 1
Complète les positions des tokens pour les entités "SITE_WEB" dans les données.

"""
