import spacy

TEXT = "I was reading the NLP books"

"""
Q5: Use spacy to determine the lemma, POS and morphology of each word in this sentence.
"""

def dissect(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    for token in doc:
        print(f"Token: {token.text}\n\t Lemma: {token.lemma_} \n\t POS: {token.pos_} \n\t {token.morph.to_dict()}")
    
dissect(TEXT)