# https://medium.com/@ageitgey/natural-language-processing-is-fun-9a0bff37854e
# utilisation de la librairie spaCy https://spacy.io/
# s'installe dans C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Lib\site-packages\spacy
# télécharger les packages de langues en allant dans un éditeur de commande (cmd, Windows PowerShell) en mode administrateur,
# dans le répertoire python C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64 et lancer la commande python
# python -m spacy download fr_core_news_md
# tous les modèles sont dans https://spacy.io/models par exemple https://spacy.io/models/fr



import spacy
nlp = spacy.load('fr_core_news_md')

text = """Toulon est une commune du Sud-Est de la France, chef-lieu du département du Var et siège de sa préfecture.
    Troisième ville de la région Provence-Alpes-Côte d'Azur derrière Marseille et Nice, elle abrite en outre le siège 
    de la préfecture maritime de la Méditerranée. La commune est établie sur les bords de la mer Méditerranée, le long 
    de la rade de Toulon. Ses habitants sont appelés les Toulonnais.
    """

doc = nlp(text) # doc contient une version parsée (analyse syntaxique) du texte.
                # nlp(text) constructeur d'un objet de class nlp aussi appelé 'doc'

# Demonstration of Name Entity Recognition = NER
for entity in doc.ents:
    print(f"{entity.text} ({entity.label_})") #https://cito.github.io/blog/f-strings/

