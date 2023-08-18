"""
Combinaison de prédictions et de règles

Combiner des prédictions issues de modèles statistiques avec des systèmes basés sur des règles
est l'un des trucs les plus importants à avoir dans ta boite à outils de NLP.

Les modèles statistiques sont utiles si ton application a besoin d'être capable de généraliser à partir de quelques exemples.

Les approches basées sur des règles sont en revanche pratiques
quand il y a un nombre plus ou moins limité d'éléments que tu veux trouver.
Par exemple, tous les pays ou toutes les villes du monde, des noms de médicaments ou encore des races de chiens.

"""
import spacy
from spacy.tokens import Span

# Charge un plus grand pipeline avec les vecteurs
nlp = spacy.load("fr_core_news_md")
# Recherche de motifs sur la base de règles
# Initialise avec le vocabulaire partagé
from spacy.matcher import Matcher, PhraseMatcher

matcher = Matcher(nlp.vocab)

# Les motifs sont des listes de dictionnaires décrivant les tokens
pattern = [{"LEMMA": "chérir", "POS": "VERB"}, {"LOWER": "les"}, {"LOWER": "chats"}]
matcher.add("AIME_CHATS", [pattern])

# Les opérateurs peuvent spécifier combien de fois un token doit être trouvé
pattern = [{"TEXT": "très", "OP": "+"}, {"TEXT": "heureux"}]
matcher.add("TRES_HEUREUX", [pattern])

# L'appel du matcher sur le doc retourne une liste de tuples
# composés avec (match_id, début, fin)
doc = nlp("Je chéris les chats et je suis très très heureux")
matches = matcher(doc)

# Ajout de prédictions statistiques
matcher = Matcher(nlp.vocab)
matcher.add("CHIEN", [[{"LOWER": "bouvier"}, {"LOWER": "bernois"}]])
doc = nlp("J'ai un Bouvier bernois")

# Voici un exemple de règle de matcher pour "golden retriever".
# Si nous itérons sur les correspondances retournées par le matcher,
# nous pouvons obtenir l'identifiant de la correspondance,
# ainsi que les indices de début et de fin du span en correspondance. Nous pouvons ensuite obtenir plus d'informations sur lui. Les objets Span nous donnent accès au document original et à tous les autres attributs des tokens et fonctionnalités linguistiques prédites par un modèle.
# Par exemple, nous pouvons obtenir le token racine du span.
# Si le span est composé de plus d'un token, ce sera le token qui décide la catégorie de la phrase.
# Par exemple, la racine de "Bouvier bernois" est "Bouvier". Nous pouvons aussi trouver la tête de la racine.
# C'est le "parent" syntaxique qui commande la phrase - dans le cas présent, le verbe "avoir".
# Enfin, nous pouvons inspecter le token précédent et ses attributs.
# Ici c'est un déterminant, l'article "un".
for match_id, start, end in matcher(doc):
    span = doc[start:end]
    print("Span en correspondance :", span.text)
    # Obtiens le token racine du span et le token de tête de la racine
    print("Token racine :", span.root.text)
    print("Token de tête de la racine :", span.root.head.text)
    # Obtiens le token précédent et son étiquette de partie de discours
    print("Token précédent :", doc[start - 1].text, doc[start - 1].pos_)

# le PhraseMatcher est comme les expressions régulières ou la recherche par mot-clé – mais avec l'accès aux tokens !
# Accepte des objets Doc en motifs
# Au lieu d'une liste de dictionnaires, on lui passe un objet Doc comme motif.
# Plus efficace et rapide que le Matcher
# Parfait pour rechercher de grandes listes de mots

matcher = PhraseMatcher(nlp.vocab)

pattern = nlp("Bouvier bernois")
matcher.add("CHIEN", [pattern])
doc = nlp("J'ai un Bouvier bernois")

# Itère sur les correspondances
for match_id, start, end in matcher(doc):
    # Obtiens le span en correspondance
    span = doc[start:end]
    print("Span en correspondance :", span.text)

doc = nlp(
    "Twitch Prime, le programme pour les membres d'Amazon destiné aux "
    "fans de jeux vidéos, arrête l'une de ses fonctionnalités les plus "
    "appréciées de cette offre tout-compris : l'absence de publicité. "
    "La nouvelle ne concerne pas les fans d'Amazon Music ni le programme "
    "pour enfants Amazon Kids. Mais cette décision montre à quel point "
    "l'intérêt des offres tout-compris peut rapidement évoluer quand les "
    "services proposés viennent à être modifiés."
)

# Crée les motifs de correspondance
# Pattern1 pour qu’il trouve correctement toutes les mentions quelle que soit la casse pour "Amazon" suivi d’un nom propre commençant par une majuscule.
pattern1 = [{"LOWER": "amazon"}, {"IS_TITLE": True, "POS": "PROPN"}]
# Pattern2 pour qu’il trouve correctement toutes les mentions d’un nom suivi de "tout-compris" quelle que soit sa casse.
pattern2 = [{"POS": "NOUN"}, {"LOWER": "tout-compris"}]

# Initialise le Matcher et ajoute les motifs
matcher = Matcher(nlp.vocab)
matcher.add("PATTERN1", [pattern1])
matcher.add("PATTERN2", [pattern2])

# Itère sur les correspondances
for match_id, start, end in matcher(doc):
    # Affiche le nom de la chaine et le texte de la portion en correspondance
    print(doc.vocab.strings[match_id], doc[start:end].text)

# Il est très important de faire
# bien attention à la tokenisation quand tu utilises le 'Matcher' basé sur les
# tokens. Parfois il est bien plus facile de rechercher simplement des chaines
# exactes et d'utiliser le 'PhraseMatcher', comme nous allons le faire dans le
# prochain exercice.
# with open("exercises/fr/countries.json", encoding="utf8") as f:
#   COUNTRIES = json.loads(f.read())
# with open("exercises/fr/country_text.txt", encoding="utf8") as f:
#   TEXT = f.read()
COUNTRIES = [
    "Afghanistan",
    "Afrique du Sud",
    "Albanie",
    "Algérie",
    "Allemagne",
    "Andorre",
    "Angola",
    "Antigua-et-Barbuda",
    "Arabie saoudite",
    "Argentine",
    "Arménie",
    "Australie",
    "Autriche",
    "Azerbaïdjan",
    "Bahamas",
    "Bahreïn",
    "Bangladesh",
    "Barbade",
    "Belgique",
    "Bélize",
    "Bénin",
    "Bhoutan",
    "Biélorussie",
    "Birmanie",
    "Bolivie",
    "Bosnie-Herzégovine",
    "Botswana",
    "Brésil",
    "Brunei",
    "Bulgarie",
    "Burkina",
    "Burundi",
    "Cambodge",
    "Cameroun",
    "Canada",
    "Cap-Vert",
    "Centrafrique",
    "Chili",
    "Chine",
    "Chypre",
    "Colombie",
    "Comores",
    "Congo",
    "République démocratique du Congo",
    "Îles Cook",
    "Corée du Nord",
    "Corée du Sud",
    "Costa Rica",
    "Côte d'Ivoire",
    "Croatie",
    "Cuba",
    "Danemark",
    "Djibouti",
    "République dominicaine",
    "Dominique",
    "Égypte",
    "Émirats arabes unis",
    "Équateur",
    "Érythrée",
    "Espagne",
    "Estonie",
    "Eswatini",
    "États-Unis",
    "Éthiopie",
    "Fidji",
    "Finlande",
    "France",
    "Gabon",
    "Gambie",
    "Géorgie",
    "Ghana",
    "Grèce",
    "Grenade",
    "Guatémala",
    "Guinée",
    "Guinée équatoriale",
    "Guinée-Bissao",
    "Guyana",
    "Haïti",
    "Honduras",
    "Hongrie",
    "Inde",
    "Indonésie",
    "Irak",
    "Iran",
    "Irlande",
    "Islande",
    "Israël",
    "Italie",
    "Jamaïque",
    "Japon",
    "Jordanie",
    "Kazakhstan",
    "Kénya",
    "Kirghizstan",
    "Kiribati",
    "Kosovo",
    "Koweït",
    "Laos",
    "Lésotho",
    "Lettonie",
    "Liban",
    "Libéria",
    "Libye",
    "Liechtenstein",
    "Lituanie",
    "Luxembourg",
    "Macédoine du Nord",
    "Madagascar",
    "Malaisie",
    "Malawi",
    "Maldives",
    "Mali",
    "Malte",
    "Maroc",
    "Îles Marshall",
    "Maurice",
    "Mauritanie",
    "Mexique",
    "Micronésie",
    "Moldavie",
    "Monaco",
    "Mongolie",
    "Monténégro",
    "Mozambique",
    "Namibie",
    "Nauru",
    "Népal",
    "Nicaragua",
    "Niger",
    "Nigéria",
    "Niue",
    "Norvège",
    "Nouvelle-Zélande",
    "Oman",
    "Ouganda",
    "Ouzbékistan",
    "Pakistan",
    "Palaos",
    "Panama",
    "Papouasie-Nouvelle-Guinée",
    "Paraguay",
    "Pays-Bas",
    "Pérou",
    "Philippines",
    "Pologne",
    "Portugal",
    "Qatar",
    "Roumanie",
    "Royaume-Uni",
    "Russie",
    "Rwanda",
    "Saint-Christophe-et-Niévès",
    "Sainte-Lucie",
    "Saint-Marin",
    "Saint-Vincent-et-les-Grenadines",
    "Salomon",
    "Salvador",
    "Samoa",
    "Sao Tomé-et-Principe",
    "Sénégal",
    "Serbie",
    "Seychelles",
    "Sierra Leone",
    "Singapour",
    "Slovaquie",
    "Slovénie",
    "Somalie",
    "Soudan",
    "Soudan du Sud",
    "Sri Lanka",
    "Suède",
    "Suisse",
    "Suriname",
    "Syrie",
    "Tadjikistan",
    "Tanzanie",
    "Tchad",
    "Tchéquie",
    "Thaïlande",
    "Timor oriental",
    "Togo",
    "Tonga",
    "Trinité-et-Tobago",
    "Tunisie",
    "Turkménistan",
    "Turquie",
    "Tuvalu",
    "Ukraine",
    "Uruguay",
    "Vanuatu",
    "Vatican",
    "Vénézuéla",
    "Vietnam",
    "Yémen",
    "Zambie",
    "Zimbabwé",
]

nlp = spacy.blank("fr")
doc = nlp("La Tchéquie pourrait aider la Slovaquie à protéger son espace aérien")

# Importe le PhraseMatcher et initialise-le
from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

# Crée des motifs objets Doc et ajoute-les au matcher
# C'est la version rapide de : [nlp(country) for country in COUNTRIES]
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", patterns)

# Appelle le matcher sur le document de test et affiche le résultat
matches = matcher(doc)
print([doc[start:end] for match_id, start, end in matches])

TEXT = """Les premières bases de l'architecture internationale d'après-guerre sont posées le 14 août 1941 avec la 
signature de la Charte de l'Atlantique par le président des États-Unis et le premier ministre du Royaume-Uni. La 
Déclaration des Nations unies fut signée le 1er janvier 1942 à Washington DC par 26 États se battant contre les 
forces de l'Axe. C'est la première fois que l'expression « Nations unies », dont la paternité est attribuée à 
Roosevelt, est utilisée ; elle désigne alors l'engagement des signataires à contribuer ensemble à l'effort de guerre 
et à ne pas signer de paix séparée avec l'Axe. Mais ça n'est qu'avec les conférences de Moscou et Téhéran que la 
Chine, les États-Unis, l'Union soviétique et le Royaume-Uni reconnaissent formellement « la nécessité d'établir 
aussitôt que possible, en vue de la paix et de la sécurité internationales, une organisation internationale fondée 
sur le principe de l'égalité souveraine de tous les États pacifiques ». Les quatre États se rencontrèrent ensuite à 
deux reprises, lors des conférences de Dumbarton Oaks et de Yalta, afin d'adopter une proposition de traité. Pour ne 
pas reproduire l'échec de la Société des Nations, il fut convenu que la nouvelle organisation devait être structurée 
autour d'un noyau dur d'États détenant une puissance objective et disposant d'un droit de véto. Finalement, 
ces cinq pays furent ceux considérés comme les vainqueurs de la Seconde Guerre mondiale : les États-Unis, la France, 
l'URSS (remplacée par la Russie en 1991), la Chine et le Royaume-Uni. Le 21 juin 1945, les États ayant signé la 
Déclaration des Nations unies et déclaré la guerre à l'Allemagne et au Japon avant mars 1945 sont invités à 
participer à la conférence de San Francisco. La rencontre s'achève le 26 juin avec la signature de la Charte des 
Nations unies. En 1956, le déploiement de la Force d'urgence des Nations unies (FUNU) en Égypte pour endiguer la 
crise du canal de Suez marque ainsi un premier tournant : c'est la première mission d'interposition armée. Dans ce 
prolongement, le déploiement de l'Opération des Nations unies au Congo (ONUC) est d'une plus grande envergure : 20 
000 casques bleus sont mobilisés au Congo, contre 6 000 en Égypte. Le mandat de l'ONUC est le premier à briser le 
principe de neutralité du maintien de la paix et les Nations unies rencontrent des difficultés tactiques, financières 
et humaines sur le terrain : 250 membres du personnel sont tués, dont le Secrétaire général. L'expérience est un 
traumatisme pour l'institution, autant chez les fonctionnaires que les États-membres, et laisse place à une période 
relativement non-interventionniste jusqu'en 1989. La décennie des années 1990 est marquée par la fin de la guerre 
froide et l'éclatement du bloc de l'Est : 30 nouveaux États membres intègrent l'organisation. Pour endiguer des 
conflits naissants, des mandats sont votés pour déployer des opérations de maintien de la paix en Yougoslavie, 
au Rwanda, en Somalie et en Angola."""

nlp = spacy.load("fr_core_news_sm")
matcher = PhraseMatcher(nlp.vocab)
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", patterns)

# Crée un doc et réinitialise les entités existantes
doc = nlp(TEXT)
doc.ents = []

# Itère sur les correspondances
for match_id, start, end in matcher(doc):
    # Crée un Span avec le label pour "GPE"
    span = Span(doc, start, end, label="GPE")

    # Actualise doc.ents avec l'ajout du span
    doc.ents = list(doc.ents) + [span]

    # Obtiens la tête de la racine du span
    span_root_head = span.root.head
    # Affiche le texte de la tête de la racine et le texte du span
    print(span_root_head.text, "-->", span.text)

# Affiche les entités dans le document
print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "GPE"])
