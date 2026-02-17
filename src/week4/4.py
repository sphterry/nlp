import sys
from random import random
from nltk.util import ngrams
from nltk.probability import FreqDist
from nltk.corpus import gutenberg

# Q3: Study this code and run it, with cmdline arg 2, 3, 4. explain what it does

START = '<s>'
END = '</s>'
TEXT = 'austen-emma.txt'
# gutenberg - Collection of public domains works
words = set(gutenberg.words(TEXT)).union([END]) # ands end symbol to set of words but not start symbol ?
sentences = gutenberg.sents(TEXT)

# Counts frequencies of a given N-grams on the text
def train(N):
    grams = []
    grams_past = []
    # go through each sentence
    for sen in sentences:
        # ear mark start and end of the sentence
        # repeat start n - 1 times, so there is padding when forming ngrams
        sentence = [START] * (N-1) + sen + [END]
        # adds n grams to list
        grams += ngrams(sentence, N) # n-grams
        grams_past += ngrams(sentence, N-1) # prefix to the n grams. for C
    freqs = FreqDist(grams)
    freqs_past = FreqDist(grams_past)
    return freqs, freqs_past

# calculates probability of a word being added to a past set
def nextprob(past, word, freqs, freqs_past):
    # add a word to something previously seen
    longer = past + [word]
    # caclulate the conditional probability of the new, longer text given the old text
    return freqs[tuple(longer)] / freqs_past[tuple(past)]

# Generates a random sentence using a random probability threshold and the frequency counts from the corpora
def generate(N, freqs, freqs_past):
    sentence = [START] * (N-1)  # initialise with padding
    while sentence[-1] != END:
        r = random() # random number used as a probability threshold
        acc = 0
        # get first past n-gram
        past = sentence[-(N-1):]
        for word in words:
            # calculate probability of this word given the previous
            acc += nextprob(past, word, freqs, freqs_past)
            if r < acc:
                # add word to the sentence 
                sentence += [word]
                break
    return sentence

# Call with argument 2, or 3, or 4, ...
if __name__=="__main__":
    N = int(sys.argv[1])
    freqs, freqs_past = train(N) # training with n-grams, returns freq of n grams and freq of n-1 grams
    generate(N, freqs, freqs_past)
    print(" ".join((generate(N, freqs, freqs_past)[(N-1):-1])))