import nltk
from nltk.corpus import brown
from nltk.probability import FreqDist

# Q6
CATS = ["news"]

def get_most_freq(values, thresh=15):
    freq = FreqDist(values)
    return freq.most_common(thresh)

def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        # IN -> Preposition
        # DT -> Determner
        if t1 == 'IN' and t2 == 'DT' and t3 == 'NN':
            print(w1, w2, w3) 

tagged_words = brown.tagged_words(categories=CATS)

# 15 most frequent tags
tags = [tag for (_, tag) in tagged_words]
print(get_most_freq(tags))

# 15 most frequent nouns
nouns = [word for (word, tag) in tagged_words if tag.startswith("NN")]
print(get_most_freq(nouns))

# words that can be plural nouns (NNS) OR third person singular verbs (VBZ) (ie: deals, files)
other = [word for (word, tag) in tagged_words if tag == "NNS" or tag=="VBZ"]
print(get_most_freq(other))

# sequences of words matching IN + DT + NN
for sentence in brown.tagged_sents(categories=CATS):
   process(sentence)