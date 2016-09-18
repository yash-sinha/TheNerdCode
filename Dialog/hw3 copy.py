from nltk.model import LaplaceNgramModel
# from nltk.probability import LidstoneProbDist
# import string
import nltk
from nltk.model import count_ngrams
from nltk.model import build_vocabulary
from nltk.corpus import gutenberg
# sents = gutenberg.sents("Gettysburg")
inputfile_gettysburg = open("Gettysburg.txt")
inputfile_firstInaugral = open("firstInaugral.txt")
inputfile_secondInaugral = open("secondInaugral.txt")
gettysburg=inputfile_gettysburg.read()
firstInaugral=inputfile_firstInaugral.read()
secondInaugral=inputfile_secondInaugral.read()
corpus1=gettysburg+firstInaugral
# print corpus1[:5]
# train = [word.lower() for word in corpus1]
# test = [word.lower() for word in secondInaugral]
# # gutenberg.sents
# test_words = corpus1.split()#[w for s in corpus for w in s]
# # print test_words[:5]

sents = gutenberg.sents("firstInaugral.txt")
sents1= gutenberg.sents("secondInaugral.txt")
nm_sent=gutenberg.sents("mandelaFreedom.txt")
nm_sent1=gutenberg.sents("mandelaPrepared.txt")
nm_sent2=gutenberg.sents("mandelaANC.txt")

nmtotal=nm_sent1+nm_sent
test_nm_sents=nmtotal[0:]
test_nm_sents1=nm_sent1[0:]
test_sents1=sents1[0:]
test_sents = sents[0:]
test_words1 = [w for s in test_sents for w in s]
test_words_nm = [w for s in test_nm_sents for w in s]
test_words_nm1 = [w for s in nm_sent2 for w in s]

# print test_words1
# print test_sents

# Some of the most annoying bugs in the old implementation occurred when an ngram model encountered
# words it had not seen during training. The conventional way to deal with this is by creating a 
# vocabulary of "known" tokens (words) before you start training.
# As you train your ngram model, you look up the tokens in the vocabulary and increment their counts 
# if they are present, otherwise increment the counter for a special UNKNOWN token. The idea is that if 
# you encounter an unseen token during testing, you can use the counts from UNKNOWN to estimate its score.
# This vocabulary can be created from data other than the one you train on.

# fdist = nltk.FreqDist(w for w in train)
# vocabulary = set(map(lambda x: x[0], filter(lambda x: x[1] >= 5, fdist.iteritems())))

# train = map(lambda x: x if x in vocabulary else "*unknown*", train)
# test = map(lambda x: x if x in vocabulary else "*unknown*", test)


# estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2) 
# vocab = build_vocabulary(2, test_words)
# print len(vocab)
# print vocab['the']
# bigram_counts = count_ngrams(2, vocab, corpus)
# print "count"
# print sorted(bigram_counts.ngrams[2].conditions())
# bigram_model = MLENgramModel(bigram_counts)
# print bigram_model.ngram_counter == bigram_counts
# # lm = NgramModel(3, brown.words(categories='news'), estimator)
# print "perplexity(test) =", bigram_model.perplexity(train)
# print bigram_model.score("last", ["the"])
# print bigram_model.score("be", ["cannot"])


corpus = [word.lower() for word in corpus1.split()]

# Train on 95% f the corpus and test on the rest
# spl = 95*len(corpus)/100
train = corpus
test = secondInaugral;

# Remove rare words from the corpus
fdist = nltk.FreqDist(w for w in train)
vocabulary = set(map(lambda x: x[0], filter(lambda x: x[1] >= 5, fdist.iteritems())))

train = map(lambda x: x if x in vocabulary else "*unknown*", train)
test = map(lambda x: x if x in vocabulary else "*unknown*", test)

vocab = build_vocabulary(5, test_words1)
print len(vocab)
bigram_counts = count_ngrams(2, vocab, test_sents)
print "count"
# print sorted(bigram_counts.ngrams[2].conditions())
bigram_model = LaplaceNgramModel(bigram_counts);
print bigram_model.ngram_counter == bigram_counts
# lm = NgramModel(3, brown.words(categories='news'), estimator)
print "perplexity(test) =", bigram_model.perplexity(test)
print sents1

vocabnm = build_vocabulary(5, test_words_nm)
print len(vocabnm)
bigram_counts_nm = count_ngrams(2, vocabnm, test_nm_sents)
print "count"
# print sorted(bigram_counts.ngrams[2].conditions())
bigram_model_nm = LaplaceNgramModel(bigram_counts_nm);
print bigram_model_nm.ngram_counter == bigram_counts_nm
# lm = NgramModel(3, brown.words(categories='news'), estimator)
print "perplexity(test) =", bigram_model_nm.perplexity(train)

print "perplexity(test) =", bigram_model_nm.perplexity(test_words_nm1)
# print bigram_model.score("last", ["the"])
# print bigram_model.score("be", ["cannot"])
