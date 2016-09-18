from nltk.model import LaplaceNgramModel
import nltk
from nltk.model import count_ngrams
from nltk.model import build_vocabulary
from nltk.corpus import gutenberg

# inputfile_gettysburg = open("Gettysburg.txt")
# inputfile_firstInaugral = open("firstInaugral.txt")
# inputfile_secondInaugral = open("secondInaugral.txt")

# gettysburg=inputfile_gettysburg.read()
# firstInaugral=inputfile_firstInaugral.read()
# secondInaugral=inputfile_secondInaugral.read()

# LB_Train_Corpus = gettysburg + firstInaugral

sents_gettysburg = gutenberg.sents("Gettysburg.txt")
sents_firstInaugral = gutenberg.sents("firstInaugral.txt")
sents_secondInaugral= gutenberg.sents("secondInaugral.txt")

inputfile_Gettysburg = open("Gettysburg.txt")
Gettysburg=inputfile_Gettysburg.read()
inputfile_firstInaugral= open("firstInaugral.txt")
firstInaugral=inputfile_firstInaugral.read()
lincolnTotal =  Gettysburg + firstInaugral
inputfile_secondInaugral = open("secondInaugral.txt")
#inputfile_secondInaugral.read()

LB_Train_Corpus = sents_gettysburg + sents_firstInaugral
train_words_lb = [w for s in LB_Train_Corpus for w in s]
test_words_lb = [w for s in sents_secondInaugral for w in s]

# Remove rare words from the corpus
vocab = build_vocabulary(5, train_words_lb)
LB_Train=map(lambda x: x in vocab, train_words_lb)
LB_Test=map(lambda x: x in vocab, test_words_lb)
bigram_counts = count_ngrams(2, vocab, LB_Train_Corpus)
LB = LaplaceNgramModel(bigram_counts)

#***************************************************

sents_nm_freedom = gutenberg.sents("mandelaFreedom.txt")
sents_nm_prepared = gutenberg.sents("mandelaPrepared.txt")
sents_nm_anc = gutenberg.sents("mandelaANC.txt")
inputfile_mandelaFreedom = open("mandelaFreedom.txt")
mandelaFreedom=inputfile_mandelaFreedom.read()
inputfile_mandelaPrepared = open("mandelaPrepared.txt")
mandelaPrepared=inputfile_mandelaPrepared.read()
mandelaTotal =  mandelaFreedom + mandelaPrepared
inputfile_mandelaANC = open("mandelaANC.txt")
# MB_Test=inputfile_mandelaANC.read()


MB_Train_Corpus =sents_nm_freedom + sents_nm_prepared
train_words_nm = [w for s in MB_Train_Corpus for w in s]
test_words_mb = [w for s in sents_nm_anc for w in s]

# Remove rare words from the corpus
vocabnm = build_vocabulary(5, train_words_nm)
print 'articles' in vocabnm
MB_Train=map(lambda x: x in vocabnm, train_words_nm)
MB_Test=map(lambda x: x in vocabnm, test_words_mb)

bigram_counts_nm = count_ngrams(2, vocabnm, MB_Train_Corpus)
MB = LaplaceNgramModel(bigram_counts_nm)

print "1b) Perplexity of LB on 2nd Inaugral", LB.perplexity(LB_Test)
print "1d) Perplexity of MB on MB-test", MB.perplexity(MB_Test)
print "1e) Perplexity of LB on LB-train", LB.perplexity(LB_Train)
print "1e) Perplexity of MB on MB-train", MB.perplexity(MB_Train)
print "1f) Perplexity of MB on LB-test", MB.perplexity(LB_Test)
print "1f) Perplexity of LB on MB-test", LB.perplexity(MB_Test)

