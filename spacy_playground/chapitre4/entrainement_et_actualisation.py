"""
Entraînement et actualisation des modèles

Entraînement et à mise à jour des composants de pipelines de spaCy
et de leurs modèles de réseaux de neurones,
et les données dont on a besoin pour le faire
- en se concentrant spécifiquement sur le reconnaisseur d'entités nommées.

Pourquoi mettre à jour le modèle ?
    _ Meilleurs résultats sur un domaine spécifique

    _ Entraînement de schémas de classification spécifiques à un problème

    _ Essentiel pour la classification de texte

    _ Très utile pour la reconnaissance d'entités nommées

    _ Moins critique pour l'étiquetage de partie de discours et l'analyse des relations de dépendances

Comment fonctionne l'entraînement
    1 _ *Initialise* les poids du modèle aléatoirement
        SpaCy permet l'actualisation de modèles existants avec plus d'exemples,
        et l'entraînement de nouveaux modèles.
        Si nous ne démarrons pas avec un pipeline entraîné,
        nous commençons par initialiser les poids aléatoirement.
    2 _ *Prédit* quelques exemples avec les poids courants
        spaCy appel nlp.update, qui prédit une série d'exemples avec les poids courants.
    3 _ *Compare* les prédictions avec les vrais labels
        Le modèle compare ensuite les prédictions avec les bonnes réponses
    4 _ *Calcule* comment changer les poids pour améliorer les prédictions
        Le modèle décide comment changer les poids pour effectuer de meilleures prédictions les fois suivantes.
    5 _ *Modifie* légèrement les poids
        Enfin nous effectuons une petite correction aux poids courants et passons au lot d'exemples suivant.
    6 _ Retourne au point 2.
        paCy continue ensuite d'appeler nlp.update sur chaque lot d'exemples des données.
        Pendant l'entraînement, on effectue généralement plusieurs passes sur les données
        pour entraîner jusqu'à ce que le modèle cesse de s'améliorer.

    Les données d'apprentissage sont les exemples avec lesquels nous voulons actualiser le modèle.

    Le texte doit être une phrase, un paragraphe ou un document plus long.
    Pour un résultat optimal, il doit être similaire à ce que le modèle rencontrera en production.

    Le label est ce qu'on veut que le modèle prédise.
    Il peut s'agir d'une catégorie de texte, ou d'un span d'entité et son type.

    Le gradient est la manière dont nous devons modifier le modèle pour réduire l'erreur actuelle.
    Il est calculé quand nous comparons les labels prédits avec les vrais labels.

    À l'issue de l'apprentissage, nous pouvons enregistrer un modèle actualisé et l'utiliser dans notre application.

Exemple : Entraînement de l'entity recognizer
    _ L'entity recognizer reconnaît des mots et des phrases en contexte

    _ Chaque token peut seulement faire partie d'une entité
        Les entités ne peuvent pas se chevaucher

    _ Les exemples doivent être fournis avec le contexte

        doc = nlp("L'iPhone 12 arrive bientôt")

        doc.ents = [Span(doc, 1, 3, label="GADGET")]

    _ Les textes dépourvus d'entités sont importants aussi

        doc = nlp("Il me faut un nouveau téléphone ! Des suggestions à me faire ?")

        doc.ents = []

    _ But : apprendre au modèle à généraliser

Les données d'entraînement
    _ Exemples de ce qu'on veut que le modèle prédise en contexte

    _ Actualise un modèle existant : quelques centaines à quelques milliers d'exemples

    _ Entraîne une nouvelle catégorie : quelques milliers à un million d'exemples

        _ les modèles anglais de spaCy : 2 millions de mots
         labellisés avec des étiquettes de partie de discours, des relations de dépendance et des entités nommées.

    _ Généralement créés manuellement par des annotateurs humains

    _ Peut être semi-automatisé – par exemple, en utilisant le Matcher de spaCy !
        _ Un linguiste computationnel peut faire ça très bien
        _ Autre exemple: se baser sur un modèle de base pour fournir des annotations,
            les faire valider/retyper/effacer par un annotateur dans une UI,
            puis les envoyer au modèle. RQ: il pourrait être judicieux d'également annoter les annotations fausses
            pour que la machine se "rappelle" de ses erreurs passées.

Données d'entraînement vs. d'évaluation
    _ Données d'entraînement : utilisés pour actualiser le modèle

    _ Données d'évaluation :
        _ données non vues par le modèle pendant l'entraînement

        _ utilisées pour calculer la précision du modèle

        _ doivent être représentatives des données que le modèle rencontrera en production

Astuce : Conversion de tes données
    *spacy convert* te permet de convertir des corpus depuis des formats courants
    supporte .conll, .conllu, .iob et l'ancien format JSON de spaCy
    $ python -m spacy convert ./train.gold.conll ./corpus
"""

# Génération d'un corpus d'entraînement (1)
import spacy
from numpy import random
from spacy.tokens import Span, DocBin

nlp = spacy.blank("fr")

# Crée un Doc avec des spans d'entités
doc1 = nlp("L'iPhone 12 arrive bientôt")
doc1.ents = [Span(doc1, 1, 3, label="GADGET")]
# Crée un autre Doc sans spans d'entités
doc2 = nlp("Il me faut un nouveau téléphone ! Des suggestions à me faire ?")

docs = [doc1, doc2]  # et ainsi de suite...

# spaCy peut être actualisé avec des données dans le même format que celui qu'il crée : des objets Doc. On a déjà
# appris à créer des objets Doc et Span dans le chapitre 2. Dans cet exemple, on crée deux objets Doc pour notre
# corpus : un qui contient une entité et un autre qui ne contient aucune entité. Pour ajouter les entités au Doc,
# on peut ajouter un Span aux doc.ents. Bien sûr, il faudra beaucoup d'autres exemples pour entraîner efficacement un
# modèle à généraliser et à prédire des entités similaire en contexte. Selon la tâche, on aura normalement besoin
# d'au moins quelques centaines à quelques milliers d'exemples représentatifs.

# Génération d'un corpus d'entraînement (2)
# Séparer les données en deux parties :
# _ données d'entraînement : utilisées pour actualiser le modèle
# _ données de développement : utilisées pour évaluer le modèle
random.shuffle(docs)
train_docs = docs[:len(docs) // 2]
dev_docs = docs[len(docs) // 2:]

# Comme mentionné précédemment, nous n'avons pas seulement besoin de données pour entraîner le modèle.
# Nous voulons aussi pouvoir évaluer sa précision sur des exemples qu'il n'a pas rencontrés pendant son entraînement.
# Cela se fait généralement en mélangeant et en séparant les données en deux :
# une partie pour l'entraînement et une pour l'évaluation.
# Ici nous utilisons une répartition simple à 50/50.

# Génération d'un corpus d'entraînement (3)
# _ DocBin: conteneur pour stocker et sauvegarder efficacement les objets Doc
# _ peut être sauvé sous forme de fichier binaire
# _ les fichiers binaires sont utilisés pour l'entraînement
# Crée et sauve un ensemble de documents pour l'entraînement
train_docbin = DocBin(docs=train_docs)
train_docbin.to_disk("./train.spacy")
# Crée et sauve un ensemble de documents pour l'évaluation
dev_docbin = DocBin(docs=dev_docs)
dev_docbin.to_disk("./dev.spacy")

# En général on voudra stocker tes données d'entraînement et de développement sous forme de fichiers sur disque,
# pour pouvoir les charger au cours du processus d'entraînement de spaCy.

# Le DocBin est un conteneur pour stocker et sérialiser efficacement les objets Doc. On peut l'instancier avec une
# liste d'objets Doc et appeler sa méthode to_disk pour le sauver sous forme de fichier binaire. On utilise
# typiquement l'extension .spacy pour ces fichiers.

# Comparé à d'autres protocoles de sérialisation binaire comme pickle, le DocBin est plus rapide et génère des
# tailles de fichiers plus réduites parce qu'il stocke seulement une fois le vocabulaire partagé.
# Voir documentation: https://spacy.io/api/docbin
