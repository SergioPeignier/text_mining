# text_mining
Some exploration regarding text mining with R
# Notes: Digital Humanities 
+ Surtout années 2000
+ Il existent des masters qui se développent
+ Travail commun informaticies et des gens de sciences humaines
+ Il exte une grosse communauté, et un contexte dérriere les textes
exemples:

+ CLAPI, corpus de langues parlées en interaction, interactional corpora
+ SyMoGiH Système Modulaire de Gestion de l'information Historique
+ Data Journalism
    + Fact checking
    + Communautées de partis
    + Analyse des médias
    + Huffington post (bloggers + journalistes)
    + Étude comparative des articles de différents pays (les themes utilisés)
    + Diffusion de l'information
+ Autres thematiques
    + Chronolines project
    + Étude des métaphores en geographie
    + Analyse de blogs
    + Réseaux sociaux
+ Opinion mining sur les sites de vente
+ Filtrage collaboratif
+ Web mining
+ Scientométrie, cartografier les sources d'info (Guillaume Cabana)
+ Brevets: souvent les gens ne prénent que l'abstract et les références
+ Business intelligence
+ Data lakes / No-sql / MongoDB
    + On garde toutes les données (texte, image, ...) -> data lake
    + On fait des requetes pour chercher ce qu'on veut
    + On analyse ce qu'on a séléctionné (Data mining, machine learning)
+ LEs textes one des points charactéristiques:
    + Les mots se suivent
+ PB data mining:
    + Représentation des données (comment représenter un texte? Évolution du texte? Mots clés ... trop?)
    + Curse of dimensionality:
        + Large vocabulary
        + Les mots ont des liens entre eux
        + Polysemie (antonomie, meronomie, metonomie)
        + Pairwise comparison
        
    + Representation learning: 
        + Apprendre la meilleure façon de représenter un objet => Quelles choses extraire du texte (se baser sur les adjectifs? les verbes? ...)
        + Combiner informations hétérogènes
    + Intégrer les Ontologies (integrating domain knowledge)
    + Rôle de validation
        + Gap sémentique (ironie, méthaphores, ...)
        
+ Disciplines:
    + Statistiques
    + Linguistiques
    + IA
    + Information retrieval IR
    + NLP
    + Computational linguistics
    + [Semantic web](http://wiki.dbpedia.org)
    + Machine Learning / Deep Learning
    
+ Content analysis: images + son + video + texte
+ Wordnet/ wikipedia


## Representation:
+ n-grams (successions de n lettres)
+ Mots
+ expressions (suites de mots: n-grams de mots)
+ concept
+ Result clustering: clusty; carrot2, kartoo

+ Web access filtering
    + Netprotect I & II
    + Spam filtering
+ Text Summarization
    + Selection based
    + Knowledge based
    + sumly
+ Information extraction & Relation extraction
    + Detecter dans une information dans un texte (donne moi toutes les informations qui parlent de ça ou ça)
    + babelfy project
+ Question answering
+ Opinion mining
    + R. Lebret RNN
    + ClimaPinion (par rapport au changement climatique)
    + Pulseweb
+ Recomendation automatique
+ Traduction automatique