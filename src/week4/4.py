import sys
from random import random
from nltk.util import ngrams
from nltk.probability import FreqDist
from nltk.corpus import gutenberg

START = '<s>'
END = '</s>'
TEXT = 'austen-emma.txt'
words = set(gutenberg.words(TEXT)).union([END])
sentences = gutenberg.sents(TEXT)

def train(N):
    grams = []
    grams_past = []
    for sen in sentences:
        sentence = [START] * (N-1) + sen + [END]
        grams += ngrams(sentence, N)
        grams_past += ngrams(sentence, N-1)
    freqs = FreqDist(grams)
    freqs_past = FreqDist(grams_past)
    return freqs, freqs_past

def nextprob(past, word, freqs, freqs_past):
    longer = past + [word]
    return freqs[tuple(longer)] / freqs_past[tuple(past)]

def generate(N, freqs, freqs_past):
    sentence = [START] * (N-1)
    while sentence[-1] != END:
        r = random()
        acc = 0
        past = sentence[-(N-1):]
        for word in words:
            acc += nextprob(past, word, freqs, freqs_past)
            if r < acc:
                sentence += [word]
                break
    return sentence

# Call with argument 2, or 3, or 4, ...
if __name__=="__main__":
    N = int(sys.argv[1])
    freqs, freqs_past = train(N)
    generate(N, freqs, freqs_past)
    print(" ".join((generate(N, freqs, freqs_past)[(N-1):-1])))