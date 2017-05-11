import sys
import os
import pickle as p

# Tokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
maupassant_text = open("maupassant_texte_pure_test.txt","r").read()
tokenized_maupassant = sent_tokenize(maupassant_text)
tokenized_maupassant_sentences = [word_tokenize(t) for t in tokenized_maupassant]
tokenized_maupassant_sentences = [[word for word in sentence if word.isalnum()] for sentence in tokenized_maupassant_sentences]
p.dump(tokenized_maupassant_sentences,open("tokenized_maupassant_sentences","wb"))

# Part of Speech 
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

# Erase Stop words
from nltk.corpus import stopwords
french_stop_words = set(stopwords.words("french")+[u'les',u'le',u'ces'])
pos_maupassant_sentences = p.load(open("POS_maupassant_sentences","rb"))
pos_maupassant_sentences = [[[word.lower() for word in words] for words in sentence] for sentence in pos_maupassant_sentences]
pos_not_stop_maupassant_sentences = [["_".join(word) for word in sentence if word[0] not in french_stop_words] for sentence in pos_maupassant_sentences ]

# LDA
from gensim import corpora, models
dictionary = corpora.Dictionary(pos_not_stop_maupassant_sentences)
corpus = [dictionary.doc2bow(sentence) for sentence in pos_not_stop_maupassant_sentences]
ldamodel = models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary, passes=20)
print(ldamodel.print_topics(num_topics=3, num_words=10))
