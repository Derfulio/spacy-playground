"""
Configuration et exécution de l'entraînement

Configuration de l'entraînement
    _ source unique de vérité pour tous les paramètres

    _ généralement nommée config.cfg

    _ définit comment initialiser l'objet nlp

    _ comprend tous les paramètres des composants du pipeline et leurs implémentations de modèles

    _ configure le processus d'entraînement et les hyperparamètres

    _ rend ton entraînement reproductible

Génération d'une configuration
    _ spaCy peut auto-générer un fichier de configuration par défaut pour toi

    _ widget de démarrage rapide interactif dans la doc: https://spacy.io/usage/training#quickstart

    _ commande init config en ligne de commande: https://spacy.io/api/cli#init-config

    $ python -m spacy init config ./config.cfg --lang fr --pipeline ner

    _ init config : la commande à exécuter

    _ config.cfg : le chemin vers lequel sauver la configuration générée

    _ --lang : la classe de langue du pipeline, par ex. fr pour le français

    _ --pipeline : les noms des composants à inclure, séparés par des virgules

Entraînement d'un pipeline
    _ tout ce dont tu as besoin est le config.cfg et les données d'entraînement et de développement

    _ les paramètres de configuration peuvent être modifiés en ligne de commande

    $ python -m spacy train ./config.cfg --output ./output --paths.train train.spacy --paths.dev dev.spacy
    -->Tu peux aussi modifier différents paramètres de configuration depuis la ligne de commande.
    $ python -m spacy train ./exercises/fr/config_gadget.cfg --output ./output --paths.train ./exercises/fr/train_gadget.spacy --paths.dev ./exercises/fr/dev_gadget.spacy

    _ train : la commande à exécuter

    _ config.cfg : le chemin vers le fichier de configuration

    _ --output : le chemin vers le répertoire de sortie où sauver le pipeline entraîné

    _ --paths.train : modifie le chemin vers les données d'entraînement

    _ --paths.dev : modifie le chemin vers les données d'évaluation

Entraînement d'un pipeline (2)
Voici un exemple d'affichage de ce que tu verras pendant et après un entraînement.
Chaque passe sur les données est appelée une "epoch", la colonne "E"
Pour chaque epoch, spaCy affiche les scores de précision tous les 200 exemples (configurable).
Le score le plus intéressant à surveiller est le score combiné dans la dernière colonne.
Il reflète à quel point ton modèle prédit précisément les bonnes réponses pour les données d'évaluation.

L'entraînement se poursuit jusqu'à ce que le modèle cesse de s'améliorer et s'arrête automatiquement.
============================ Training pipeline ============================
ℹ Pipeline: ['tok2vec', 'ner']
ℹ Initial learn rate: 0.001

E   #       LOSS TOK2VEC    LOSS        NER ENTS_F  ENTS_P  ENTS_R  SCORE

--- ------  ------------    --------    ------  ------  ------  ------

  0       0          0.00     26.50    0.73    0.39    5.43    0.01

  0     200         33.58    847.68   10.88   44.44    6.20    0.11

  1     400         70.88    267.65   33.50   45.95   26.36    0.33

  2     600         67.56    156.63   45.32   62.16   35.66    0.45

  3     800        138.28    134.12   48.17   74.19   35.66    0.48

  4    1000        177.95    109.77   51.43   66.67   41.86    0.51

  6    1200         94.95     52.13   54.63   67.82   45.74    0.55

  8    1400        126.85     66.19   56.00   65.62   48.84    0.56

 10    1600         38.34     24.16   51.96   70.67   41.09    0.52

 13    1800        105.14     23.23   56.88   69.66   48.06    0.57

✔ Saved pipeline to output directory
/path/to/output/model-last


Chargement d'un pipeline entraîné
    _ le résultat après entraînement est un pipeline spaCy chargeable normal

        _ model-last : le dernier pipeline entraîné
        _ model-best : le meilleur pipeline entraîné

    _ chargement avec spacy.load


    import spacy

    nlp = spacy.load("/path/to/output/model-best")
    doc = nlp("iPhone 11 vs iPhone 8 : quelle sont les différences ?")
    print(doc.ents)

Astuce : Ton pipeline sous forme de package
    _ spacy package: crée un package Python installable contenant ton pipeline
        https://spacy.io/api/cli#package
    _ facile à versionner et à déployer

    $ python -m spacy package /path/to/output/model-best ./packages --name mon_pipeline --version 1.0.0
    $ cd ./packages/fr_mon_pipeline-1.0.0
    $ pip install dist/fr_mon_pipeline-1.0.0.tar.gz

    Charge et utilise le pipeline après installation:

    nlp = spacy.load("fr_mon_pipeline")


"""
import spacy.cli.train

spacy.cli.train.train()