import spacy
nlp = spacy.load('fr_core_news_md')

text = """Toulon est une commune du Sud-Est de la France, chef-lieu du département du Var et siège de sa préfecture.
    Troisième ville de la région Provence-Alpes-Côte d'Azur derrière Marseille et Nice, elle abrite en outre le siège 
    de la préfecture maritime de la Méditerranée. La commune est établie sur les bords de la mer Méditerranée, le long 
    de la rade de Toulon. Ses habitants sont appelés les Toulonnais.
    """

# Demonstration of a data scrubber
# remplace tous les lieux (LOC) par -- EFFACE --

# remplace un token par "-- EFFACE-- " si c'est un lieu
def replace_name_with_placeholder(token):
    if token.ent_iob != 0 and token.ent_type_ == "LOC":
        return "-- EFFACE --"
    else:
        return token.string

# loop through all the entities in a document and check if they are location
def scrub(text):
    doc = nlp(text)
    for ent in doc.ents:
        ent.merge()
    tokens = map(replace_name_with_placeholder,doc)
    return "".join(tokens)

print(scrub(text))
