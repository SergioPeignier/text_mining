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

## Libraries
+ nlp java: Lucen
+ sentiment analysis: 
+ summary: 

## Stemming et lemmatization
+ Porter stemmer, regles en cascade (snowballC en R)
+ regles morphologiques automatiques qui coupent des sufixes
+ lemmatization base sur des dictionnaires
+ readPDF (librairies TM de R)



https://cran.r-project.org/web/packages/slam/slam.pdf
http://search.carrot2.org

http://nbviewer.jupyter.org/github/Velcin/TM-lecture/blob/master/TM-lecture-export.ipynb
http://wiki.dbpedia.org
https://www.w3.org/2001/sw/wiki/Category:Semantic_Web_Browser
http://dbarneche.github.io/2014-12-11-ufsc/lessons/01-intro_r/data-structures.html
http://stackoverflow.com/questions/9637278/r-tm-package-invalid-input-in-utf8towcs
http://gijn.org/2016/06/27/a-poor-journalists-text-mining-toolkit/
Huffington post
http://symogih.org


+ C'est mieux d'utiliser des 1-grams (mots tous seuls) que des n-grams ... ou des combinaisons des deux
+ http://tubo.lirmm.fr/biotex/
+ Para lod score es una buena idea uniformizar

# Topic modeling
+ Algebrique
	+ EN realidad un objeto (un texto) es una composicion de varios temas al mismo tiempo
	+ Latent semantic analysis, NMF
	+ Deerwaster et al. 90
	+ Non negative matrix factorization. lee et al. 1999 2001 => plus facile a interpreter
	+ SVD est un elargissement de PCA
	
+ Geometric model derivees de distances
	+ TDT
	+ AGAPE
+  Probabiliste approaches
	+ pLSA
	+ LDA
	+ Modeles probabilistes: A. McCallum
+ Interesting:
	+ topic detection and tracking
+ Datasets
	+ Dataset tang et al. titre et abstract de plein de papiers scientifiques
	+ En general ils sont disponibles les datasets des journaux (abstract et nom)
	+ http://paperscape.org/
+ Tests
	+ Palmeto java ... coherence thematiques
	+ topic labeling
+ Conseils:
	+ Des textes courts:
		+ clustetering / ou variantes de LDA qui considerent que ce n'est que une mixture de 2 thematiques (contexte et theme)
		
		
# Interesting dataset
+ markov chain monte carlo
+ non negative matrix factorization
+ topic learning
+ temporal mixture model
+ Conditional random field