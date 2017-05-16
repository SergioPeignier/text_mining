import sys
import os
import pickle as p

# Tokenizer
# https://www.tutorialspoint.com/python/string_isalnum.htm
from nltk.tokenize import sent_tokenize, word_tokenize
maupassant_text = open("maupassant_texte_pure_test.txt","r").read()
tokenized_maupassant = sent_tokenize(maupassant_text)
tokenized_maupassant_sentences = [word_tokenize(t) for t in tokenized_maupassant]
tokenized_maupassant_sentences = [[word for word in sentence if word.isalnum()] for sentence in tokenized_maupassant_sentences]
p.dump(tokenized_maupassant_sentences,open("tokenized_maupassant_sentences","wb"))

# [Part of Speech](https://nlp.stanford.edu/software/tagger.html)
# http://stackoverflow.com/questions/8590370/how-to-do-pos-tagging-using-the-nltk-pos-tagger-in-python
# http://www.nltk.org/api/nltk.tag.html#module-nltk.tag.stanford
# http://stackoverflow.com/questions/29556109/spanish-pos-tagging-with-stanford-nlp-is-it-possible-to-get-the-person-number
# https://web.archive.org/web/20160325024315/http://nlp.lsi.upc.edu/freeling/doc/tagsets/tagset-es.html
from nltk.tag.stanford import StanfordPOSTagger
tokenized_maupassant_sentences = p.load(open("tokenized_maupassant_sentences","rb"))
french_tagger = '/Users/peigniersergio/Documents/stanford-postagger-full-2016-10-31/models/french.tagger'
postagger_program = '/Users/peigniersergio/Documents/stanford-postagger-full-2016-10-31/stanford-postagger.jar'
french_postagger = StanfordPOSTagger(french_tagger,postagger_program)
#pos_maupassant_sentences = [french_postagger.tag(sentence) for sentence in tokenized_maupassant_sentences[1:100]]
pos_maupassant_sentences = []
for i,sentence in enumerate(tokenized_maupassant_sentences[1:100]):
	pos_maupassant_sentences.append(french_postagger.tag(sentence))
	if i%10 == 0:
		print i,len(tokenized_maupassant_sentences)
print pos_maupassant_sentences
p.dump(pos_maupassant_sentences,open("POS_maupassant_sentences","wb"))

# [CoreNLP](https://stanfordnlp.github.io/CoreNLP/)
# https://stanfordnlp.github.io/CoreNLP/corenlp-server.html
# https://github.com/smilli/py-corenlp
# Run server java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000` in /Users/peigniersergio/Documents/stanford-corenlp-full-2016-10-31
"""
from pycorenlp import StanfordCoreNL
text = 'Pusheen and Smitha walked along the beach. Pusheen wanted to surf, but fell off the surfboard.'
nlp = StanfordCoreNLP('http://localhost:9000')
output = nlp.annotate(text, properties={
  'annotators': 'tokenize,ssplit,pos,depparse,parse',
  'outputFormat': 'json'
  })
print(output['sentences'][0]['parse'])
"""

# [Wordnet](https://wordnet.princeton.edu/wordnet/download/current-version/#nix)
# http://wordnetweb.princeton.edu/perl/webwn?s=dog&sub=Search+WordNet&o2=&o0=1&o8=1&o1=1&o7=&o5=&o9=&o6=&o3=&o4=&h=000000
# NLTK wordnet http://www.nltk.org/howto/wordnet.html
# from nltk.corpus import wordnet as wn
# wn.synsets('dog')

# It is also possible to use babelnet https://github.com/aghie/pybabelfy
# http://babelnet.org/login
"""
from pybabelfy.babelfy import *
text= "BabelNet is both a multilingual encyclopedic dictionary and a semantic network"
lang = "EN"
key = "KEY" #This only works for the demo example. Change it for your RESTful key (you must register at babelfy.org for it)
babelapi = Babelfy()
semantic_annotations = babelapi.disambiguate(text,lang,key)
"""

# Erase Stop words
# http://stackoverflow.com/questions/5486337/how-to-remove-stop-words-using-nltk-or-python
from nltk.corpus import stopwords
french_stop_words = set(stopwords.words("french")+[u'les',u'le',u'ces'])
pos_maupassant_sentences = p.load(open("POS_maupassant_sentences","rb"))
pos_maupassant_sentences = [[[word.lower() for word in words] for words in sentence] for sentence in pos_maupassant_sentences]
pos_not_stop_maupassant_sentences = [["_".join(word) for word in sentence if word[0] not in french_stop_words] for sentence in pos_maupassant_sentences ]

# LDA
# https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html
from gensim import corpora, models
dictionary = corpora.Dictionary(pos_not_stop_maupassant_sentences)
corpus = [dictionary.doc2bow(sentence) for sentence in pos_not_stop_maupassant_sentences]
ldamodel = models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary, passes=20)
print(ldamodel.print_topics(num_topics=3, num_words=10))
