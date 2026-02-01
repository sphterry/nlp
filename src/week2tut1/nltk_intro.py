from nltk.book import *

def deconstruct_string(s):
    # token -> word, punctuation, technical name for sequence of chars
    print(f"Text has {len(s)} tokens")
    
    # sorted set of vocabulary words (list begins with punctuation)
    words = sorted(set(s))
    
    # word type -> form or spelling of a word independent from its specific occurrences
    print(f"Text has {len(words)} types")
    
    print(f"Text has lexical richness of {len(words)/ len(s)}")

    # Q2: print alphabetically sorted list of all words that consist of entirely capital letters and are more than 5 chars
    res = sorted(w for w in words if w.isupper() and len(w) > 5)
    print(res)

deconstruct_string(text6)