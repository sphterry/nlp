import spacy
from nltk.tokenize import WordPunctTokenizer

# Q3 tokenise this text in spacy and nltk, compare:
TEXT = "E.g. I.B.M.’s CEO wrote at 14:15: ’Yesterday’s speech by Dr. J.-L. O’Neill II didn’t deserve an A+!’."

def spacy_tokenise(s):
    nlp = spacy.blank("en")

    for token in nlp(s):
        print(token)

def nltk_tokenise(s):
    tokeniser = WordPunctTokenizer()

    for token in tokeniser.tokenize(s):
        print(token)

print("Spacy tokens:")
spacy_tokenise(TEXT)

print("NLTK tokens:")
nltk_tokenise(TEXT)

"""
Mistakes in NLTK tokenisation:
 - 'E.g.' is split into characters
 - the . from 'I.B.M.' and the quote after it are considered one token
 - 14:15 is split up into 14, :, 15
 - the . is taken off Dr.
 - O'Neill is split
 - didn't -> didn, ', t instead of did, n't
 - all the punctuation at the end is grouped
"""