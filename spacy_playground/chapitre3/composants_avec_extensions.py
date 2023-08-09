"""
Composants avec extensions

Les extensions d’attributs sont particulièrement puissantes quand elles sont combinées avec des composants de pipeline personnalisés. Dans cet exercice, tu vas écrire un composant de pipeline qui trouve des noms de pays et une extension personnalisée qui retourne le nom de la capitale du pays, s’il est disponible.

Un matcher de phrases avec tous les pays est proposé via la variable matcher. Un dictionnaire des pays avec leurs capitales en correspondance est proposé via la variable CAPITALS.

_ Complète le composant countries_component_function et crée un Span avec le label "GPE" (entité géopolitique)
pour toutes les correspondances.

_ Ajoute le composant au pipeline.

_ Déclare l’extension d’attribut Span nommée "capital" avec le getter get_capital.

_ Traite le texte et affiche le texte de l’entité, le label de l’entité,
et la capitale de l’entité pour chaque span d’entité de doc.ents.

"""

COUNTRIES = ['Afghanistan', 'Afrique du Sud', 'Albanie', 'Algérie', 'Allemagne', 'Andorre', 'Angola', 'Antigua-et-Barbuda', 'Arabie saoudite', 'Argentine', 'Arménie', 'Australie', 'Autriche', 'Azerbaïdjan', 'Bahamas', 'Bahreïn', 'Bangladesh', 'Barbade', 'Belgique', 'Bélize', 'Bénin', 'Bhoutan', 'Biélorussie', 'Birmanie', 'Bolivie', 'Bosnie-Herzégovine', 'Botswana', 'Brésil', 'Brunei', 'Bulgarie', 'Burkina', 'Burundi', 'Cambodge', 'Cameroun', 'Canada', 'Cap-Vert', 'Centrafrique', 'Chili', 'Chine', 'Chypre', 'Colombie', 'Comores', 'Congo', 'République démocratique du Congo', 'Îles Cook', 'Corée du Nord', 'Corée du Sud', 'Costa Rica', "Côte d'Ivoire", 'Croatie', 'Cuba', 'Danemark', 'Djibouti', 'République dominicaine', 'Dominique', 'Égypte', 'Émirats arabes unis', 'Équateur', 'Érythrée', 'Espagne', 'Estonie', 'Eswatini', 'États-Unis', 'Éthiopie', 'Fidji', 'Finlande', 'France', 'Gabon', 'Gambie', 'Géorgie', 'Ghana', 'Grèce', 'Grenade', 'Guatémala', 'Guinée', 'Guinée équatoriale', 'Guinée-Bissao', 'Guyana', 'Haïti', 'Honduras', 'Hongrie', 'Inde', 'Indonésie', 'Irak', 'Iran', 'Irlande', 'Islande', 'Israël', 'Italie', 'Jamaïque', 'Japon', 'Jordanie', 'Kazakhstan', 'Kénya', 'Kirghizstan', 'Kiribati', 'Kosovo', 'Koweït', 'Laos', 'Lésotho', 'Lettonie', 'Liban', 'Libéria', 'Libye', 'Liechtenstein', 'Lituanie', 'Luxembourg', 'Macédoine du Nord', 'Madagascar', 'Malaisie', 'Malawi', 'Maldives', 'Mali', 'Malte', 'Maroc', 'Îles Marshall', 'Maurice', 'Mauritanie', 'Mexique', 'Micronésie', 'Moldavie', 'Monaco', 'Mongolie', 'Monténégro', 'Mozambique', 'Namibie', 'Nauru', 'Népal', 'Nicaragua', 'Niger', 'Nigéria', 'Niue', 'Norvège', 'Nouvelle-Zélande', 'Oman', 'Ouganda', 'Ouzbékistan', 'Pakistan', 'Palaos', 'Panama', 'Papouasie-Nouvelle-Guinée', 'Paraguay', 'Pays-Bas', 'Pérou', 'Philippines', 'Pologne', 'Portugal', 'Qatar', 'Roumanie', 'Royaume-Uni', 'Russie', 'Rwanda', 'Saint-Christophe-et-Niévès', 'Sainte-Lucie', 'Saint-Marin', 'Saint-Vincent-et-les-Grenadines', 'Salomon', 'Salvador', 'Samoa', 'Sao Tomé-et-Principe', 'Sénégal', 'Serbie', 'Seychelles', 'Sierra Leone', 'Singapour', 'Slovaquie', 'Slovénie', 'Somalie', 'Soudan', 'Soudan du Sud', 'Sri Lanka', 'Suède', 'Suisse', 'Suriname', 'Syrie', 'Tadjikistan', 'Tanzanie', 'Tchad', 'Tchéquie', 'Thaïlande', 'Timor oriental', 'Togo', 'Tonga', 'Trinité-et-Tobago', 'Tunisie', 'Turkménistan', 'Turquie', 'Tuvalu', 'Ukraine', 'Uruguay', 'Vanuatu', 'Vatican', 'Vénézuéla', 'Vietnam', 'Yémen', 'Zambie', 'Zimbabwé']
CAPITALS = {'Afghanistan': 'Kaboul', 'Afrique du Sud': 'Prétoria', 'Albanie': 'Tirana', 'Algérie': 'Alger', 'Allemagne': 'Berlin', 'Andorre': 'Andorre-la-Vieille', 'Angola': 'Luanda', 'Antigua-et-Barbuda': "Saint John's", 'Arabie saoudite': 'Riyad', 'Argentine': 'Buenos Aires', 'Arménie': 'Erevan', 'Australie': 'Canberra', 'Autriche': 'Vienne', 'Azerbaïdjan': 'Bakou', 'Bahamas': 'Nassau', 'Bahreïn': 'Manama', 'Bangladesh': 'Dacca', 'Barbade': 'Bridgetown', 'Belgique': 'Bruxelles', 'Bélize': 'Belmopan', 'Bénin': 'Porto-Novo', 'Bhoutan': 'Thimphou', 'Biélorussie': 'Minsk', 'Birmanie': 'Naypyidaw', 'Bolivie': 'Sucre / La Paz', 'Bosnie-Herzégovine': 'Sarajevo', 'Botswana': 'Gaborone', 'Brésil': 'Brasilia', 'Brunei': 'Bandar Seri Begawan', 'Bulgarie': 'Sofia', 'Burkina': 'Ouagadougou', 'Burundi': 'Gitega', 'Cambodge': 'Phnom Penh', 'Cameroun': 'Yaoundé', 'Canada': 'Ottawa', 'Cap-Vert': 'Praia', 'Centrafrique': 'Bangui', 'Chili': 'Santiago', 'Chine': 'Pékin', 'Chypre': 'Nicosie', 'Colombie': 'Bogota', 'Comores': 'Moroni', 'Congo': 'Brazzaville', 'République démocratique du Congo': 'Kinshasa', 'Îles Cook': 'Avarua', 'Corée du Nord': 'Pyongyang', 'Corée du Sud': 'Séoul', 'Costa Rica': 'San José', "Côte d'Ivoire": 'Yamoussoukro', 'Croatie': 'Zagreb', 'Cuba': 'La Havane', 'Danemark': 'Copenhague', 'Djibouti': 'Djibouti', 'République dominicaine': 'Saint-Domingue', 'Dominique': 'Roseau', 'Égypte': 'Le Caire', 'Émirats arabes unis': 'Abou Dabi', 'Équateur': 'Quito', 'Érythrée': 'Asmara', 'Espagne': 'Madrid', 'Estonie': 'Tallinn', 'Eswatini': 'Mbabané', 'États-Unis': 'Washington', 'Éthiopie': 'Addis Abeba', 'Fidji': 'Suva', 'Finlande': 'Helsinki', 'France': 'Paris', 'Gabon': 'Libreville', 'Gambie': 'Banjul', 'Géorgie': 'Tbilissi', 'Ghana': 'Accra', 'Grèce': 'Athènes', 'Grenade': 'Saint-Georges', 'Guatémala': 'Guatémala', 'Guinée': 'Conakry', 'Guinée équatoriale': 'Malabo', 'Guinée-Bissao': 'Bissao', 'Guyana': 'Georgetown', 'Haïti': 'Port-au-Prince', 'Honduras': 'Tégucigalpa', 'Hongrie': 'Budapest', 'Inde': 'New Delhi', 'Indonésie': 'Jakarta', 'Irak': 'Bagdad', 'Iran': 'Téhéran', 'Irlande': 'Dublin', 'Islande': 'Reykjavik', 'Israël': '', 'Italie': 'Rome', 'Jamaïque': 'Kingston', 'Japon': 'Tokyo', 'Jordanie': 'Amman', 'Kazakhstan': 'Nour-Soultan', 'Kénya': 'Nairobi', 'Kirghizstan': 'Bichkek', 'Kiribati': 'Bairiki', 'Kosovo': 'Pristina', 'Koweït': 'Koweït', 'Laos': 'Vientiane', 'Lésotho': 'Maséru', 'Lettonie': 'Riga', 'Liban': 'Beyrouth', 'Libéria': 'Monrovia', 'Libye': 'Tripoli', 'Liechtenstein': 'Vaduz', 'Lituanie': 'Vilnius', 'Luxembourg': 'Luxembourg', 'Macédoine du Nord': 'Skopje', 'Madagascar': 'Antananarivo (Tananarive)', 'Malaisie': 'Kuala Lumpur', 'Malawi': 'Lilongwé', 'Maldives': 'Malé', 'Mali': 'Bamako', 'Malte': 'La Valette', 'Maroc': 'Rabat', 'Îles Marshall': 'Delap-Uliga-Darrit', 'Maurice': 'Port-Louis', 'Mauritanie': 'Nouakchott', 'Mexique': 'Mexico', 'Micronésie': 'Palikir', 'Moldavie': 'Chisinau', 'Monaco': 'Monaco', 'Mongolie': 'Oulan-Bator', 'Monténégro': 'Podgorica', 'Mozambique': 'Maputo', 'Namibie': 'Windhoek', 'Nauru': 'Yaren', 'Népal': 'Katmandou', 'Nicaragua': 'Managua', 'Niger': 'Niamey', 'Nigéria': 'Abuja', 'Niue': 'Alofi', 'Norvège': 'Oslo', 'Nouvelle-Zélande': 'Wellington', 'Oman': 'Mascate', 'Ouganda': 'Kampala', 'Ouzbékistan': 'Tachkent', 'Pakistan': 'Islamabad', 'Palaos': 'Melekeok', 'Panama': 'Panama', 'Papouasie-Nouvelle-Guinée': 'Port Moresby', 'Paraguay': 'Assomption (Asuncion)', 'Pays-Bas': 'Amsterdam', 'Pérou': 'Lima', 'Philippines': 'Manille', 'Pologne': 'Varsovie', 'Portugal': 'Lisbonne', 'Qatar': 'Doha', 'Roumanie': 'Bucarest', 'Royaume-Uni': 'Londres', 'Russie': 'Moscou', 'Rwanda': 'Kigali', 'Saint-Christophe-et-Niévès': 'Basseterre', 'Sainte-Lucie': 'Castries', 'Saint-Marin': 'Saint-Marin', 'Saint-Vincent-et-les-Grenadines': 'Kingstown', 'Salomon': 'Honiara', 'Salvador': 'San Salvador', 'Samoa': 'Apia', 'Sao Tomé-et-Principe': 'Sao Tomé', 'Sénégal': 'Dakar', 'Serbie': 'Belgrade', 'Seychelles': 'Victoria', 'Sierra Leone': 'Freetown', 'Singapour': 'Singapour', 'Slovaquie': 'Bratislava', 'Slovénie': 'Ljubljana', 'Somalie': 'Mogadiscio', 'Soudan': 'Khartoum', 'Soudan du Sud': 'Djouba', 'Sri Lanka': 'Sri Jayewardenepura-Kotte', 'Suède': 'Stockholm', 'Suisse': 'Berne', 'Suriname': 'Paramaribo', 'Syrie': 'Damas', 'Tadjikistan': 'Douchanbé', 'Tanzanie': 'Dodoma', 'Tchad': 'Ndjamena', 'Tchéquie': 'Prague', 'Thaïlande': 'Bangkok', 'Timor oriental': 'Dili', 'Togo': 'Lomé', 'Tonga': "Nuku'alofa", 'Trinité-et-Tobago': "Port-d'Espagne (Port of Spain)", 'Tunisie': 'Tunis', 'Turkménistan': 'Achgabat', 'Turquie': 'Ankara', 'Tuvalu': 'Vaiaku', 'Ukraine': 'Kiev', 'Uruguay': 'Montévidéo', 'Vanuatu': 'Port-Vila', 'Vatican': '', 'Vénézuéla': 'Caracas', 'Vietnam': 'Hanoï', 'Yémen': 'Sanaa', 'Zambie': 'Lusaka', 'Zimbabwé': 'Hararé'}

import json
import spacy
from spacy.language import Language
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

#with open("exercises/fr/countries.json", encoding="utf8") as f:
#    COUNTRIES = json.loads(f.read())

#with open("exercises/fr/capitals.json", encoding="utf8") as f:
#    CAPITALS = json.loads(f.read())

nlp = spacy.blank("fr")
matcher = PhraseMatcher(nlp.vocab)
matcher.add("COUNTRY", list(nlp.pipe(COUNTRIES)))


@Language.component("countries_component")
def countries_component_function(doc):
    # Crée une entité Span avec le label "GPE" pour toutes les correspondances
    matches = matcher(doc)
    doc.ents = [Span(doc, start, end, label="GPE") for match_id, start, end in matches]
    return doc


# Ajoute le composant au pipeline
nlp.add_pipe("countries_component")
print(nlp.pipe_names)

# Getter qui recherche le texte du span dans le dictionnaire
# des capitales des pays
get_capital = lambda span: CAPITALS.get(span.text)

# Déclare l'extension d'attribut de Span "capital" avec le getter get_capital
Span.set_extension("capital", getter=get_capital)

# Traite le texte et affiche le texte de l'entité,
# ses attributs label et capitale
doc = nlp("La Tchéquie pourrait aider la Slovaquie à protéger son espace aérien")
print([(ent.text, ent.label_, ent._.capital) for ent in doc.ents])

# Ceci est un excellent exemple de la manière dont on peut
# ajouter des données structurées à son pipeline spaCy.


